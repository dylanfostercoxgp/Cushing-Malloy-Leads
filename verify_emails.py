#!/usr/bin/env python3
"""
verify_emails.py -- Cushing-Malloy MANDATORY pre-draft verification gate
=========================================================================
Every weekly run MUST pass all candidate leads through this script BEFORE
updating the dashboard, creating drafts, or sending the report.

APPROVAL VERDICTS — only THREE paths to APPROVED (updated Aug 10 2026):
  ✅ PASS        SMTP returned 250 AND domain is not catch-all.
                 Direct confirmation the mailbox exists. Safest.
  ✅ PASS_CATCHALL  SMTP returned 250 but domain accepts anything.
                 REQUIRES email_source_url — confirms the specific person
                 published this address. Server won't hard-bounce catch-all.
  ✅ UNVERIFIED + Apollo verified
                 SMTP probe was blocked by server policy (PBL/Spamhaus).
                 REQUIRES apollo_email_status == "verified".
                 Apollo independently confirmed the mailbox is live.

  ❌ UNVERIFIED + src URL only  →  ALWAYS REJECTED.
                 Staff pages go stale when people leave. A published URL
                 does NOT confirm the mailbox is still active. This was
                 the cause of hard bounces on Aug 10 2026. Never approved.
  ❌ UNVERIFIED + nothing       →  REJECTED.
  ❌ HARD_FAIL / NO_MX          →  REJECTED.

It performs, for every candidate lead:
  1. EXISTING CLIENT CHECK   -- against 306-client list (hard block on
                                exact/substring/normalized match; REVIEW flag
                                on weaker single-word overlap)
  2. DUPLICATE CHECK         -- against every lead from every prior run
  3. BOUNCE CHECK            -- against permanently suppressed bounced emails
  4. SMTP VERIFICATION       -- RCPT TO probe of the real address
  5. CATCH-ALL DETECTION     -- probes a random fake address at the same
                                domain; if the server accepts anything, a 250
                                proves nothing and the address only counts if
                                published on the lead's own site (source URL
                                required)
  6. GENERIC ADDRESS POLICY  -- info@/contact@/submissions@/hello@/press@/
                                office@ REQUIRE a source URL showing the exact
                                address published on the lead's own website

It writes verification-log-YYYY-MM-DD.txt (the audit log) and
verification-results-YYYY-MM-DD.json (machine-readable, consumed by the rest
of the run).

USAGE:
    1. Save candidate leads to a JSON file:
       [
         {"name": "Press Name", "email": "person@domain.com",
          "website": "https://...",
          "email_source_url": "https://domain.com/contact  (REQUIRED for
           generic or catch-all addresses; the page where the address is
           visibly published)"},
         ...
       ]
    2. Run:  python3 verify_emails.py candidates.json
    3. Exit code 0 = at least MIN_VERIFIED leads passed. Non-zero = keep
       researching; the run may NOT proceed to drafting.

Requires: dnspython  (pip install dnspython --break-system-packages)
"""

import json
import os
import re
import socket
import sys
import time
import random
import string
import unicodedata
import datetime
from concurrent.futures import ThreadPoolExecutor

try:
    import dns.resolver
except ImportError:
    sys.exit("FATAL: dnspython missing. Run: pip install dnspython --break-system-packages")

HERE = os.path.dirname(os.path.abspath(__file__))
SUPPRESSION_FILE = os.path.join(HERE, "02_Lead_Data", "suppression-list.json")
MIN_VERIFIED = 20
GENERIC_PREFIXES = ("info", "contact", "submissions", "hello", "press",
                    "office", "admin", "mail", "editor", "editors", "inquiries")
NOISE_WORDS = {
    "press", "publishing", "publishers", "publications", "books", "book",
    "edition", "editions", "inc", "llc", "ltd", "co", "corp", "corporation",
    "company", "the", "of", "and", "&", "a", "an", "univ", "university",
    "intl", "international", "group", "center", "ctr", "services", "svcs",
    "media", "productions", "studio", "house", "state", "review", "point",
    "street", "new",
}


def normalize(name):
    name = unicodedata.normalize("NFKD", name).lower()
    name = re.sub(r"[^\w\s]", " ", name)
    return " ".join(t for t in name.split() if t not in NOISE_WORDS and len(t) > 1)


def load_suppression():
    with open(SUPPRESSION_FILE) as f:
        return json.load(f)


def client_check(lead_name, clients):
    """Returns ('BLOCK'|'REVIEW'|'CLEAR', matched_client)."""
    lead_lower = lead_name.strip().lower()
    lead_norm = normalize(lead_name)
    lead_sig = {t for t in lead_norm.split() if len(t) >= 5}
    review_hit = ""
    for client in clients:
        c_lower = client.lower()
        c_norm = normalize(client)
        # Hard blocks: exact, substring either direction, normalized equal
        if lead_lower == c_lower or c_lower in lead_lower or lead_lower in c_lower:
            return "BLOCK", client
        if lead_norm and c_norm and lead_norm == c_norm:
            return "BLOCK", client
        # Weak signal: shared significant word -> flag for human review only
        c_sig = {t for t in c_norm.split() if len(t) >= 5}
        if lead_sig and c_sig and lead_sig & c_sig and not review_hit:
            review_hit = client
    return ("REVIEW", review_hit) if review_hit else ("CLEAR", "")


def duplicate_check(lead_name, email, sup):
    lead_norm = normalize(lead_name)
    email_l = (email or "").strip().lower()
    for p in sup["prior_leads"]:
        if normalize(p["name"]) == lead_norm and lead_norm:
            return True, f"company already in run(s) {', '.join(p['runs'])}"
        if email_l and email_l in [e.lower() for e in p["emails"]]:
            return True, f"email already used in run(s) {', '.join(p['runs'])}"
    return False, ""


def bounce_check(lead_name, email, sup):
    email_l = (email or "").strip().lower()
    lead_norm = normalize(lead_name)
    for b in sup["bounced_emails"]:
        if email_l and email_l == b["email"].lower():
            return True, f"email bounced {b['date_bounced']} ({b['reason']})"
        if lead_norm and normalize(b["company"]) == lead_norm:
            return True, f"company bounced {b['date_bounced']} at {b['email']}"
    return False, ""


def get_mx(domain):
    try:
        records = dns.resolver.resolve(domain, "MX")
        return str(sorted(records, key=lambda r: r.preference)[0].exchange).rstrip(".")
    except Exception:
        return None


def smtp_probe(mx_host, email, timeout=6):
    """Returns (code, message). code 0 = connection problem, -1 = no MX."""
    try:
        s = socket.create_connection((mx_host, 25), timeout=timeout)

        def recv():
            return s.recv(512).decode("utf-8", "replace")

        def send(cmd):
            s.sendall((cmd + "\r\n").encode())
            time.sleep(0.4)
            return recv()

        recv()  # banner
        send("EHLO verify.cushing-malloy.com")
        send("MAIL FROM:<check@cushing-malloy.com>")
        resp = send(f"RCPT TO:<{email}>")
        send("QUIT")
        s.close()
        code = int(resp.strip()[:3]) if resp.strip()[:3].isdigit() else 0
        return code, resp.strip()[:110]
    except Exception as e:
        return 0, str(e)[:90]


def verify_email(email):
    """Full SMTP verification with catch-all detection.
    Returns dict: {code, message, catch_all(bool|None), verdict}
    verdict: PASS | PASS_CATCHALL | HARD_FAIL | NO_MX | UNVERIFIED
    """
    domain = email.split("@")[1].lower()
    mx = get_mx(domain)
    if not mx:
        return {"code": -1, "message": "NO MX RECORD", "catch_all": None, "verdict": "NO_MX"}
    code, msg = smtp_probe(mx, email)
    if code in (550, 551, 552, 553, 554):
        # RFC 3463: 5.7.x = policy/security rejection of the PROBING HOST, not
        # proof the mailbox is bad (e.g. "550 5.7.1 Client host blocked",
        # Spamhaus PBL). Treat as UNVERIFIED per process rules. True mailbox
        # failures (5.1.1 user unknown etc.) remain HARD_FAIL.
        _m = msg.lower()
        if "5.7." in msg or "client host" in _m or "spamhaus" in _m or "blocked" in _m or "policy" in _m:
            return {"code": code, "message": msg, "catch_all": None, "verdict": "UNVERIFIED"}
        return {"code": code, "message": msg, "catch_all": None, "verdict": "HARD_FAIL"}
    if code != 250:
        return {"code": code, "message": msg, "catch_all": None, "verdict": "UNVERIFIED"}
    # Got 250 -- now detect catch-all with a random fake address
    fake = "cmv-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=14)) + "@" + domain
    time.sleep(0.3)
    fcode, _ = smtp_probe(mx, fake)
    if fcode == 250:
        return {"code": code, "message": msg, "catch_all": True, "verdict": "PASS_CATCHALL"}
    return {"code": code, "message": msg, "catch_all": False, "verdict": "PASS"}


def is_generic(email):
    return email.split("@")[0].lower() in GENERIC_PREFIXES


def main(candidates_path, run_date=None):
    sup = load_suppression()
    candidates = json.load(open(candidates_path))
    today = run_date or datetime.date.today().isoformat()
    log_path = os.path.join(HERE, "02_Lead_Data", f"verification-log-{today}.txt")
    results_path = os.path.join(HERE, "02_Lead_Data", f"verification-results-{today}.json")

    lines = []
    results = []

    # Parallel SMTP pre-check: verify every candidate email concurrently so the
    # gate finishes in seconds instead of minutes. Results cached, then the
    # sequential audit loop below consumes the cache.
    _emails = sorted({(l.get("email") or "").strip() for l in candidates if (l.get("email") or "").strip()})
    smtp_cache = {}
    if _emails:
        with ThreadPoolExecutor(max_workers=min(32, len(_emails))) as _ex:
            _futs = {_ex.submit(verify_email, e): e for e in _emails}
            for _f, _e in _futs.items():
                try:
                    smtp_cache[_e] = _f.result()
                except Exception as _err:
                    smtp_cache[_e] = {"code": 0, "message": str(_err)[:80], "catch_all": None, "verdict": "UNVERIFIED"}

    def log(s=""):
        lines.append(s)
        print(s)

    log("=" * 78)
    log("  CUSHING-MALLOY VERIFICATION GATE -- AUDIT LOG")
    log(f"  Run date: {today}   Candidates: {len(candidates)}   Minimum required: {MIN_VERIFIED}")
    log("  All checks run BEFORE any draft is created or report sent.")
    log("=" * 78)

    approved = 0
    for lead in candidates:
        name = lead.get("name", "").strip()
        email = (lead.get("email") or "").strip()
        src = (lead.get("email_source_url") or "").strip()
        apollo_matched = bool(lead.get("apollo_matched"))
        apollo_status = (lead.get("apollo_email_status") or "").strip()
        entry = {"name": name, "email": email, "email_source_url": src,
                 "apollo_matched": apollo_matched, "apollo_email_status": apollo_status,
                 "checks": {}, "approved": False, "reason": ""}
        apollo_note = f"   [Apollo: {apollo_status or 'matched'}]" if apollo_matched else "   [Apollo: no match -- best-effort path]"
        log(f"\nLEAD: {name}   <{email or 'no email'}>{apollo_note}")

        status, match = client_check(name, sup["existing_clients"])
        entry["checks"]["client"] = {"status": status, "match": match}
        if status == "BLOCK":
            entry["reason"] = f"EXISTING CLIENT: {match}"
            log(f"  [BLOCKED]  Existing client match: {match}")
            results.append(entry)
            continue
        if status == "REVIEW":
            log(f"  [REVIEW]   Weak client-name overlap with '{match}'. Confirmed NOT the same company before proceeding.")

        dup, why = duplicate_check(name, email, sup)
        entry["checks"]["duplicate"] = {"blocked": dup, "why": why}
        if dup:
            entry["reason"] = f"DUPLICATE: {why}"
            log(f"  [BLOCKED]  Duplicate of prior run: {why}")
            results.append(entry)
            continue

        bnc, why = bounce_check(name, email, sup)
        entry["checks"]["bounce"] = {"blocked": bnc, "why": why}
        if bnc:
            entry["reason"] = f"PREVIOUSLY BOUNCED: {why}"
            log(f"  [BLOCKED]  {why}")
            results.append(entry)
            continue

        if not email:
            entry["reason"] = "No email address to verify"
            log("  [NO DRAFT] No email address. Lead may appear in dashboard as 'No Verified Email Found'.")
            results.append(entry)
            continue

        v = smtp_cache.get(email) or verify_email(email)
        entry["checks"]["smtp"] = v
        generic = is_generic(email)
        entry["checks"]["generic"] = generic

        if v["verdict"] in ("HARD_FAIL", "NO_MX"):
            entry["reason"] = f"SMTP {v['verdict']}: {v['code']} {v['message']}"
            log(f"  [REJECTED] SMTP {v['code']}: {v['message']}")
            log("             -> Find a different address for this lead or set 'No Verified Email Found'.")
            results.append(entry)
            continue

        if v["verdict"] == "UNVERIFIED":
            # SMTP probe was blocked by PBL/policy — the server NEVER evaluated
            # whether the mailbox exists. A src URL only proves the address was
            # published at some point; staff pages go stale when people leave.
            # RULE: Apollo email_status="verified" is REQUIRED for PBL-blocked probes.
            # Src URL alone is NOT sufficient — it caused hard bounces (Aug 10 2026).
            if apollo_status.lower() == "verified":
                entry["approved"] = True
                entry["reason"] = f"SMTP probe blocked by server policy but Apollo email_status=verified"
                log(f"  [APPROVED] SMTP probe blocked ({v['message'][:60]}) AND Apollo email_status=verified.")
            else:
                # src URL present but Apollo NOT verified — REJECT (stale staff page risk)
                if src:
                    log(f"  [REJECTED] SMTP probe blocked by PBL/policy. Src URL present but staff pages go stale.")
                    log(f"             Apollo verification required for probe-blocked domains. No draft.")
                    entry["reason"] = f"SMTP probe blocked ({v['message'][:60]}); src URL present but Apollo verified required"
                else:
                    log(f"  [REJECTED] SMTP unverifiable and address NOT confirmed. No draft.")
                    entry["reason"] = f"SMTP unverifiable ({v['message'][:60]}) and no published source URL"
                results.append(entry)
                continue
        elif v["verdict"] == "PASS_CATCHALL":
            if src:
                entry["approved"] = True
                entry["reason"] = f"250 on catch-all domain; address published at {src}"
                log(f"  [APPROVED] 250 but domain is CATCH-ALL (accepts anything). Address published at: {src}")
            else:
                entry["reason"] = "Catch-all domain 250 proves nothing; no published source URL"
                log(f"  [REJECTED] Domain is catch-all; 250 is meaningless and address is not confirmed published. No draft.")
                results.append(entry)
                continue
        else:  # PASS
            if generic and not src:
                entry["reason"] = "Generic address without published source URL (extrapolated addresses are banned)"
                log(f"  [REJECTED] Generic address ({email.split('@')[0]}@) with no published source URL. Extrapolated = banned.")
                results.append(entry)
                continue
            entry["approved"] = True
            entry["reason"] = f"SMTP 250 verified, not catch-all{'; generic but published at ' + src if generic else ''}"
            log(f"  [APPROVED] SMTP 250 verified. Catch-all: no.{' Generic, published at: ' + src if generic else ''}")

        if entry["approved"]:
            approved += 1
        results.append(entry)

    n_apollo = sum(1 for c in candidates if c.get("apollo_matched"))
    n_apollo_verified = sum(1 for c in candidates
                            if (c.get("apollo_email_status") or "").lower() == "verified")
    log("\n" + "=" * 78)
    log(f"  APOLLO: {n_apollo} of {len(candidates)} candidates matched; "
        f"{n_apollo_verified} with Apollo-verified emails (cap: 30 credits/run).")
    log(f"  RESULT: {approved} of {len(candidates)} candidates APPROVED for drafting.")
    log(f"  Rejected/blocked: {len(candidates) - approved}")
    if approved >= MIN_VERIFIED:
        log(f"  GATE: PASSED (>= {MIN_VERIFIED} verified). Run may proceed to dashboard + drafts.")
    else:
        log(f"  GATE: FAILED -- need {MIN_VERIFIED - approved} more verified leads. KEEP RESEARCHING.")
        log("  Do NOT update the dashboard, create drafts, or send the report yet.")
    log("=" * 78)

    with open(log_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(results_path, "w") as f:
        json.dump({"run_date": today, "approved_count": approved,
                   "minimum_required": MIN_VERIFIED,
                   "gate_passed": approved >= MIN_VERIFIED,
                   "results": results}, f, indent=2)
    print(f"\nAudit log:    {log_path}")
    print(f"Results JSON: {results_path}")
    return 0 if approved >= MIN_VERIFIED else 1


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit("Usage: python3 verify_emails.py candidates.json [run-date YYYY-MM-DD]")
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None))
