# Cushing-Malloy Lead Intelligence — Weekly Automation Process
**Client:** Cushing-Malloy Books | **Managed by:** ideaBoss | **Version:** 2.0 | **Updated:** March 2026

> **How to use this file:** Give this document to Claude (via Claude Code or Cowork mode) and say:
> *"Run the Cushing-Malloy weekly lead generation process."*
> Claude will follow every step in order, automatically.

---

## OVERVIEW

This process runs every **Monday at 3:00 AM** (or on-demand). It performs three jobs:

1. **Lead Discovery** — Research and score **20–25 new leads** across multiple channels
2. **Outreach Drafts** — Save personalized draft emails to SmarterMail Drafts folder for each verified lead (do NOT auto-send)
3. **Weekly Report** — Email a summary HTML report to dylan@coxgp.com

**Total estimated runtime:** 15–25 minutes depending on lead count.

> **Lead Volume Rule:** Each run produces between 20 and 25 leads total. The count varies naturally week to week (some runs will have 20, some 22, some 24). Do not force a fixed number — let discovery drive the count within the 20–25 range.

---

## IDENTITY & CONTEXT

You are acting as a specialized lead generation intelligence agent for **Cushing-Malloy Books** (cushing-malloy.com), a third-generation, family-owned **book manufacturing and printing company** headquartered in Ann Arbor, Michigan. Founded in 1948. Ann Arbor is the "Short Run Book Capital of America."

You are finding people who need books **physically printed** — not book buyers, reviewers, or readers.

**Outreach signature to use in all emails:**
```
Warm Regards,

Tedd Litty
C: 616-843-3825  |  T: 734.663.8554 ×103  |  F: 734.663.5731
E: tlitty@cushing-malloy.com  |  www.cushing-malloy.com
Cushing-Malloy, Inc.  |  1350 N. Main, Ann Arbor, MI 48104
Where Books Are Bound For Greatness®
```

**CC on all outreach drafts:** `tlitty@cushing-malloy.com`

---

## STEP 1 — LOAD CONTEXT FILES

Before researching leads, read these files to understand the full brief:

1. **Lead Generation Prompt (full spec):**
   `Dashboard/cushing-malloy-lead-gen-prompt.md`

2. **Current dashboard leads (to avoid duplicates):**
   `Dashboard/cushing-malloy-lead-dashboard.html`
   → Scan the `const RUNS` data block for all previously generated leads.
   → Extract all names/companies already in the system. Do NOT regenerate any of them.

**Previously generated leads (as of March 2026) — DO NOT DUPLICATE:**
Orange Frazer Press, Bottom Dog Press, Fiddlehead Press, Porkbelly Press, Bex Kitchen, Idris Doosi, Paul Jarvis, Nat Eliason, Hill Schroder, Dickie Bush, Sohee Carpenter, M.G. Hunt, Sarah Styf, Rachel Moss, Erin Romeo, New Michigan Press, Glass Poetry Press, Ice Cube Press, 42 Miles Press, Midwest Writing Center (MWC Press), Yellow Arrow Publishing, Ali Kriegsman, Allegra Hall, Rob Dircks, Maren Moore, Oriana Leckert, Cornerstone Press (UW-Stevens Point), Restless Books, Wandering in the Words Press

---

## STEP 2 — RESEARCH NEW LEADS

Using the full spec in `cushing-malloy-lead-gen-prompt.md`, research and identify **20–25 new leads**. Prioritize quality over category quotas — surface the best leads found, whether they are individual authors, content creators, or small publishers.

### Lead Volume & Scoring Composition (per run):

| Tier | Count | Score | Priority | Description |
|---|---|---|---|---|
| **Core batch** | ~20 minimum | 6–10 | High / Medium | Fully vetted, verified email, clear print signal |
| **Supplemental** | up to 5 | 1–4 | Below threshold | Lower confidence, but potentially high-value if the right person is reached |
| **Total per run** | **20–25** | — | — | Varies naturally; do not force a fixed count |

**On supplemental (below-5) leads:**
- These are NOT bad leads — they are lower-confidence leads where the print signal is indirect or the contact is harder to reach.
- Only include if there is a genuine reason to believe the right person could convert (e.g., strong audience, clear book project, just missing a direct email signal).
- Each supplemental lead must include a sentence in the Notes field explaining why it may still be valuable despite the lower score.
- If fewer than 5 strong supplemental leads exist, do not force them — quality always beats quota.

### Lead Categories to source (vary across runs, no forced ratio):
**Individual Authors & Content Creators:**
- Solo Author – Print-Ready
- Solo Author – Launch Mode
- Health & Wellness Creator
- Food & Recipe Creator
- Lifestyle Creator
- Business & Authority Author
- Social Media Creator / Book Author

**Small Publishers:**
- Micro Press (≤5 titles/yr)
- Small Press (6–20 titles/yr)
- Nonfiction Specialty Press
- Poetry & Literary Press
- Children's Book Publisher
- Hybrid Publisher / Author Services

### Discovery Channels (use at least 4–5 per run, vary each week):
1. Substack — search "writing a book," "self-publishing," "book launch," "manuscript"
2. Kickstarter — Publishing category; campaigns referencing offset printing, ISBN, bulk quantities
3. Instagram/TikTok — "book coming soon," health/food/lifestyle creators with book announcements
4. YouTube — Business, wellness, cooking, self-help channels with book announcements
5. Podcast hosts — Hosts writing books based on show themes (health, business, personal development)
6. Amazon KDP — Authors with 1–3 titles, 4+ star ratings, upgrade candidates
7. Goodreads — Author profiles, 1–3 titles, recent publication dates
8. Reddit — r/selfpublish, r/writing, r/cookbookjunkies, r/IndieAuthor
9. LinkedIn — "self-published author + book launch," "writing my first book," US geography filter
10. IBPA member signals — New members, award entrants, conference attendees
11. Poets & Writers — Small Presses database
12. Reedsy — Independent publisher directory (filtered by genre/location)
13. Bookshop.org — Indie publisher storefronts
14. State arts councils — Grant recipients in MI, OH, IL, WI, IN
15. Eventbrite / local bookstore events — Author readings and signings

### Data to collect for EVERY lead:

| Field | Instructions |
|---|---|
| **Source** | Where discovered (e.g., "Substack," "Kickstarter Book Campaign," "Instagram Health Creator") |
| **Name/Company** | Full name (author) or press name (publisher) |
| **Website** | Primary URL — website, Substack, Amazon Author Page, social profile |
| **Email** | Verified email; if not found after exhaustive search: "No Verified Email Found" |
| **Phone** | Include if found at 80%+ confidence; leave blank (not a placeholder) if not found |
| **Category** | One category from the list above |
| **Priority Score** | 1–10 using scoring formula below |
| **Notes** | 2–3 sentences: WHY this lead is valuable + specific outreach angle |

### Priority Scoring Formula (score each 0–2, weight, normalize to 1–10):

| Criterion | Weight | 0 pts | 1 pt | 2 pts |
|---|---|---|---|---|
| Print Volume Signal | 25% | No evidence | POD only / 1 book | Multiple titles OR explicit offset/bulk OR active Kickstarter |
| Contact Completeness | 20% | No contact | Email OR phone only | Email + phone + website confirmed |
| Operational Activity | 20% | Inactive | Moderate (6–12 mo ago) | Active now (book in progress, event booked, campaign live) |
| Audience & Reach | 15% | No public audience | 1K–10K followers | 10K+ followers / paid subscribers / podcast listeners |
| Geographic Reachability | 10% | International only | Central/East US | Midwest, Great Lakes, or Michigan-adjacent |
| Growth Signal | 5% | Declining/static | Stable | Growing (new book, Kickstarter funded, new imprint) |
| Contact Quality | 5% | No way to reach | Generic form only | Direct email or phone confirmed |

**RULE: Core batch must score 6 or above. Up to 5 supplemental leads scoring below 5 are permitted per run if they represent genuinely promising prospects. Leads scoring below 5 must include a justification note.**

**Priority tiers:** 8–10 = High | 5–7 = Medium | 1–4 = Low (supplemental only, max 5 per run)

---

## STEP 3 — UPDATE THE DASHBOARD HTML

1. Open `Dashboard/cushing-malloy-lead-dashboard.html`
2. Find the `const RUNS` JavaScript object near the top of the file
3. Determine today's date string in `YYYY-MM-DD` format
4. Add a new key to `RUNS` for today's date, following this exact format:

```javascript
"YYYY-MM-DD": [
  {
    source:   "Source Name",
    name:     "Lead Name or Company",
    website:  "https://website.com",
    email:    "email@example.com",
    phone:    "(555) 555-5555",
    category: "cat-health",   // see category class list below
    score:    8,
    priority: "medium",         // "high" (8-10), "medium" (5-7), "low" (1-4)
    notes:    "2-3 sentence qualifier and outreach angle."
  },
  // ... more leads
]
```

### Category CSS classes to use (match exactly):
- Solo author, print-ready: `cat-solo-ready`
- Solo author, launch mode: `cat-solo-launch`
- Health & wellness creator: `cat-health`
- Food & recipe creator: `cat-food`
- Lifestyle creator: `cat-lifestyle`
- Business & authority author: `cat-business`
- Social media creator: `cat-creator`
- Micro press: `cat-micro`
- Small press: `cat-small`
- Nonfiction specialty press: `cat-nonfiction`
- Poetry & literary press: `cat-poetry`
- Children's book publisher: `cat-childrens`
- Hybrid publisher: `cat-hybrid`

5. Update the date selector options in the HTML `<select id="dateSelect">` element to include the new date (newest first)
6. Save the updated file to `01_Dashboard/cushing-malloy-lead-dashboard.html`
7. Also copy the updated file to the root as **`index.html`** (NOT as `cushing-malloy-lead-dashboard.html`) — the root file in this folder and on GitHub is always named `index.html`

---

## STEP 4 — ARCHIVE LEAD DATA

Save a JSON snapshot of this week's leads to the archive:

1. Create file: `Dashboard/02_Lead_Data/archive/leads-YYYY-MM-DD.json`
2. Format:
```json
{
  "run_date": "YYYY-MM-DD",
  "lead_count": 15,
  "leads": [
    {
      "source": "...",
      "name": "...",
      "website": "...",
      "email": "...",
      "phone": "...",
      "category": "...",
      "score": 8,
      "priority": "medium",
      "notes": "..."
    }
  ]
}
```

---

## STEP 5 — PUSH UPDATED FILES TO GITHUB

Push all updated files to the GitHub repository so the live dashboard reflects the new run.

```bash
# Clone repo to temp directory
git clone https://ghp_YOUR_GITHUB_TOKEN_HERE@github.com/dylanfostercoxgp/Cushing-Malloy-Leads.git /tmp/cm-push-tmp

# Copy updated working dashboard into the repo's 01_Dashboard folder
cp /mnt/Cushing-Malloy/01_Dashboard/cushing-malloy-lead-dashboard.html \
   /tmp/cm-push-tmp/01_Dashboard/cushing-malloy-lead-dashboard.html

# Copy same file to root as index.html (replaces whatever was there before)
cp /mnt/Cushing-Malloy/01_Dashboard/cushing-malloy-lead-dashboard.html \
   /tmp/cm-push-tmp/index.html

# Copy the new archive JSON
cp /mnt/Cushing-Malloy/02_Lead_Data/archive/leads-$(date +%Y-%m-%d).json \
   /tmp/cm-push-tmp/02_Lead_Data/archive/

# Remove any stale root file that used the old name (if present)
rm -f /tmp/cm-push-tmp/cushing-malloy-lead-dashboard.html

# Commit and push
cd /tmp/cm-push-tmp
git config user.email "dylan@coxgp.com"
git config user.name "Dylan Cox"
git remote set-url origin https://ghp_YOUR_GITHUB_TOKEN_HERE@github.com/dylanfostercoxgp/Cushing-Malloy-Leads.git
git add -A
git commit -m "Weekly lead run — $(date +%Y-%m-%d): new leads added"
git push origin main
```

**File naming rule on GitHub:**
- `01_Dashboard/cushing-malloy-lead-dashboard.html` → pushed as-is under `01_Dashboard/`
- Root dashboard → always pushed as **`index.html`** (GitHub Pages serves this as the live URL)
- The old root file `cushing-malloy-lead-dashboard.html` does NOT exist at the repo root — remove it if found

---

## STEP 6 — CREATE SMARTERMAIL OUTREACH DRAFTS

For every lead with a **verified email address**, save a personalized draft to the SmarterMail Drafts folder using Python via IMAP. **Save as DRAFT only. Do NOT send.**

**Email account:** `printyourbook@cushing-malloy.com` — drafts appear at `https://mail.cushing-malloy.com`

### Python helper (run via Bash tool for each lead):

> **Important:** All drafts are saved to SmarterMail (`printyourbook@cushing-malloy.com`) via IMAP. **Never use Gmail.** Drafts must be HTML format to support the Cushing-Malloy.com hyperlink in the closing. After drafting all leads, run Apollo enrichment for phone numbers and add a note "No phone number found via Apollo enrichment." to the Full Notes of any lead where Apollo returns no phone data.

```python
import imaplib, email, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

IMAP_HOST = "mail.cushing-malloy.com"
IMAP_PORT = 993
EMAIL_USER = "printyourbook@cushing-malloy.com"
EMAIL_PASS = "SNaFx$os5^Z4Rig"

CC_EMAIL = "tlitty@cushing-malloy.com"

def save_draft(to_address, subject, plain_body, html_body=None):
    msg = MIMEMultipart("alternative")
    msg["From"]    = EMAIL_USER
    msg["To"]      = to_address
    msg["Cc"]      = CC_EMAIL
    msg["Subject"] = subject
    msg["Date"]    = email.utils.formatdate()
    msg.attach(MIMEText(plain_body, "plain", "utf-8"))
    if html_body:
        msg.attach(MIMEText(html_body, "html", "utf-8"))
    mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.append("Drafts", r"\\Draft", imaplib.Time2Internaldate(time.time()), msg.as_bytes())
    mail.logout()

# Call once per lead — provide both plain text and HTML versions:
# save_draft("lead@example.com", "Subject line", plain_body, html_body)
```

### Email template and personalization rules:

**Subject line formula:** `Printing [their book/project type] — [specific hook from their situation]`

Examples:
- "Printing your cookbook — short-run offset at 500 copies"
- "Printing your business book — from manuscript to 1,000 copies"
- "Your Kickstarter backers deserve a beautiful book"

**Body template (personalize every [BRACKET] — never send a generic version):**

```
Hi [First Name],

[1-2 sentences specific to THEM — reference their actual book project, audience,
Kickstarter, Instagram post, Substack, or announcement. Show you've done your
homework. Never make this generic.]

I'm reaching out from Cushing-Malloy Books in Ann Arbor, Michigan — we've been
manufacturing books since 1948, and we specialize in exactly the kind of run you're
looking at: [250/500/1,000/2,000/5,000] copies with [offset/digital] printing for
[their genre/format].

Here's what makes us different for [authors like you / presses like yours]:

- One person manages your project start to finish — same contact for quoting,
  production, proofing, and delivery. Nothing falls through the cracks.
- 20 working days from approved files to finished books, delivered to your door.
- [Insert one more specific differentiator relevant to this lead — e.g.,
  "We walk first-time authors through every step — paper selection, file prep,
  trim size, even why there are blank pages at the back." OR "We teach you the
  print run math so you make the right financial decision on quantity."]

If you're not sure where to start, that's exactly why we're here. We'd love to
give you a no-pressure quote and talk through your options.

Visit our website at Cushing-Malloy.com. We look forward to hearing from you soon.

Warm Regards,

Tedd Litty
C: 616-843-3825  |  T: 734.663.8554 ×103  |  F: 734.663.5731
E: tlitty@cushing-malloy.com  |  www.cushing-malloy.com
Cushing-Malloy, Inc.  |  1350 N. Main, Ann Arbor, MI 48104
Where Books Are Bound For Greatness®
```

> **Closing rule:** The second-to-last paragraph always ends with "Visit our website at [Cushing-Malloy.com](https://cushing-malloy.com). We look forward to hearing from you soon." — hyperlinked in HTML drafts. Never use "Would a quick call this week work?" as a closing line.

**Personalization checklist before creating each draft:**
- [ ] Subject line references their specific project
- [ ] Opening line shows you read their actual content/announcement
- [ ] Print run size estimate is realistic for their situation
- [ ] At least one differentiator is tailored to their specific need
- [ ] Tone matches their vibe (casual for creators, professional for publishers)

---

## STEP 7 — SEND WEEKLY REPORT EMAIL

Save a weekly summary draft to SmarterMail Drafts using the same `save_draft()` Python function from Step 6.

- **To:** dylan@coxgp.com
- **CC:** [CONNIE_EMAIL]

**Subject:** `Cushing-Malloy Lead Intelligence Prospecting — Week of [Monday Date]`

**Body (HTML — use exactly this structure, filling all brackets with real content):**

```html
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; max-width: 620px; margin: 0 auto; color: #2a2a2a; font-size: 14px; line-height: 1.6;">

  <!-- HEADER -->
  <div style="background-color: #3787c4; padding: 22px 26px; border-radius: 5px 5px 0 0;">
    <div style="color: rgba(255,255,255,0.75); font-size: 10px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px;">Lead Intelligence Prospecting</div>
    <div style="color: #ffffff; font-size: 24px; font-weight: bold; letter-spacing: -0.3px;">Cushing-Malloy</div>
    <div style="color: rgba(255,255,255,0.7); font-size: 12px; margin-top: 7px;">
      Week of [MONDAY DATE] &nbsp;&middot;&nbsp; Powered by <a href="https://ideaboss.io" style="color: rgba(255,255,255,0.85); text-decoration: none;">ideaboss.io</a>
    </div>
  </div>

  <!-- BODY -->
  <div style="background: #ffffff; padding: 28px 26px; border: 1px solid #dde6f0; border-top: none;">

    <p style="margin-top: 0;">Connie,</p>

    <p>This week's prospecting run surfaced <strong>[X] qualified leads</strong> across [2–3 channels used — e.g., "Substack author communities, Kickstarter book campaigns, and health creator networks on Instagram"]. Every lead was verified for print relevance, active production signals, and reachable contact information before making the list — so what you're seeing represents genuine opportunities worth a conversation.</p>

    <p>A couple worth a closer look: <strong>[Lead 1 Name]</strong> — [1 sentence on why, how found, e.g., "a food blogger with 38K Instagram followers who announced a cookbook project this month, discovered through her public content feed"]. And <strong>[Lead 2 Name]</strong> — [1 sentence, e.g., "a business coach on Substack with a paid subscriber base actively promoting an upcoming book launch, sourced from Substack's creator directory"]. Both have verified contact details and clear intent to go to print.</p>

    <!-- LEAD HIGHLIGHTS TABLE -->
    <table style="width: 100%; border-collapse: collapse; margin: 22px 0; font-size: 13px;">
      <tr style="background-color: #3787c4; color: #ffffff;">
        <th style="padding: 9px 12px; text-align: left; font-weight: 600; border-radius: 3px 0 0 0;">Name / Company</th>
        <th style="padding: 9px 12px; text-align: left; font-weight: 600;">Category</th>
        <th style="padding: 9px 12px; text-align: left; font-weight: 600; border-radius: 0 3px 0 0;">Why Qualified</th>
      </tr>
      <!-- Repeat this row for each lead — alternate row background #f4f8fc and #ffffff -->
      <tr style="background-color: #f4f8fc;">
        <td style="padding: 8px 12px; border-bottom: 1px solid #dde6f0;"><strong>[Lead Name]</strong></td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #dde6f0;">[Category]</td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #dde6f0;">[1 short qualifying sentence — why this lead matters, what signals indicated print intent]</td>
      </tr>
      <tr style="background-color: #ffffff;">
        <td style="padding: 8px 12px; border-bottom: 1px solid #dde6f0;"><strong>[Lead Name]</strong></td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #dde6f0;">[Category]</td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #dde6f0;">[1 short qualifying sentence]</td>
      </tr>
      <!-- Add all leads from this run as rows -->
    </table>

    <!-- RESEARCH SOURCES -->
    <p style="font-size: 12px; color: #777; border-top: 1px solid #e8eef4; padding-top: 14px; margin-bottom: 22px;">
      <strong style="color: #555;">Research sources this run:</strong>&nbsp;
      [Source 1 — e.g., Substack publishing community] &nbsp;&middot;&nbsp; [Source 2 — e.g., Kickstarter book campaigns]
    </p>

    <!-- CTA BUTTON -->
    <div style="text-align: center; margin: 10px 0 6px;">
      <a href="https://ideaboss.cushing-malloy.com" style="display: inline-block; background-color: #3787c4; color: #ffffff; padding: 13px 32px; border-radius: 4px; text-decoration: none; font-size: 14px; font-weight: bold; letter-spacing: 0.2px;">
        View Full Dashboard &rarr;
      </a>
    </div>

  </div>

  <!-- FOOTER -->
  <div style="background-color: #f0f5fa; padding: 14px 26px; border: 1px solid #dde6f0; border-top: none; text-align: center; font-size: 11px; color: #999; border-radius: 0 0 5px 5px;">
    Generated by <a href="https://ideaboss.io" style="color: #3787c4; text-decoration: none; font-weight: 600;">ideaboss.io</a>
    &nbsp;&middot;&nbsp; Lead Intelligence Prospecting for Cushing-Malloy Books &nbsp;&middot;&nbsp; [DATE]
  </div>

</body>
</html>
```

**Instructions for filling the template:**
- Replace `[X]` with actual lead count
- Replace `[MONDAY DATE]` and `[DATE]` with the run date (e.g., "March 31, 2026")
- In the two intro paragraphs, name 2 specific leads from this run with exactly how and where they were found
- Add one row per lead to the table — every lead from this run, no scores, no priority labels
- List exactly 2 research sources actually used in this run
- Replace `[DASHBOARD URL]` with `https://ideaboss.cushing-malloy.com` (live dashboard URL)

---

## STEP 8 — VERIFY COMPLETION

Run a final checklist before marking the process complete:

- [ ] 20–25 new leads researched and scored
- [ ] At least 20 leads score 6 or above (core batch)
- [ ] No more than 5 supplemental leads score below 5 (each with justification note)
- [ ] Best leads surfaced regardless of category type
- [ ] At least 4–5 different discovery channels used
- [ ] Leads span multiple US states/regions
- [ ] No duplicates from previous runs
- [ ] Dashboard HTML updated with new run date and leads (prepended, newest first)
- [ ] Lead archive JSON saved to `02_Lead_Data/archive/leads-YYYY-MM-DD.json`
- [ ] `01_Dashboard/cushing-malloy-lead-dashboard.html` updated
- [ ] Root `index.html` updated (copied from `01_Dashboard/` — named `index.html`, not `cushing-malloy-lead-dashboard.html`)
- [ ] All changes committed and pushed to GitHub (`01_Dashboard/` copy + `index.html` at root)
- [ ] SmarterMail outreach drafts saved for all leads with verified emails
- [ ] Weekly report draft saved to SmarterMail Drafts (To: dylan@coxgp.com)

---

## FOLDER STRUCTURE REFERENCE

```
Cushing-Malloy/
├── index.html                           ← ROOT DASHBOARD (GitHub serves this; always matches 01_Dashboard copy)
├── WEEKLY-PROCESS.md                    ← This file
├── README.md
├── Cushing-Malloy-Agent-Overview.pdf    ← 1-page overview PDF
├── ideaBoss-Lead-Intelligence-Prospecting-Guide.pdf
├── build_agent_overview.py
│
├── 01_Dashboard/
│   └── cushing-malloy-lead-dashboard.html   ← PRIMARY WORKING COPY (edit this, then copy to root as index.html)
│
├── 02_Lead_Data/
│   └── archive/
│       └── leads-YYYY-MM-DD.json            ← Weekly lead snapshots
│
├── 03_Documentation/
│   ├── cushing-malloy-lead-gen-prompt.md    ← Full agent spec
│   ├── WEEKLY-PROCESS.md                    ← Copy of this file
│   ├── Cushing-Malloy-Agent-Overview.pdf
│   └── CushingMalloy_StyleGuide.docx
│
└── 04_Reports/
    └── (weekly HTML report archives, if saved)
```

**File naming rule:**
- `01_Dashboard/cushing-malloy-lead-dashboard.html` — the working copy, always edited first
- `index.html` (root) — always a copy of the above; named `index.html` so GitHub Pages serves it correctly
- Never create or maintain a root file named `cushing-malloy-lead-dashboard.html` — that name is only used inside `01_Dashboard/`

---

## KEY CUSHING-MALLOY DIFFERENTIATORS
*(Use these in outreach emails and pitch notes)*

| Differentiator | Talking Point |
|---|---|
| Family-owned since 1948 | Third generation; deep trust, stability, reliability |
| Single point of contact | Same person from quote → production → proofing → delivery. Nothing drops. |
| White-glove guidance | Walks first-time authors through everything they don't know they don't know |
| 20 working days | From approved files to finished books, delivered |
| Starts at 250 copies | Clear price break education; 500→1,000 dramatically reduces per-unit cost |
| Volume pricing education | Teaches authors to think strategically about print run quantity |
| E-book conversion | Full upsell from print to digital — one partner for both formats |
| Offset AND digital | Flexibility for different run sizes and budgets |
| Ann Arbor, Michigan | "Short Run Book Capital of America" — genuine manufacturing heritage |
| Fox Business Manufacturing Marvels | National brand recognition and legitimacy |

---

## OUTREACH TONE GUIDE

| Lead Type | Tone | Key Angle |
|---|---|---|
| First-time author | Warm, reassuring, educational | "We hold your hand through the whole process" |
| Health/wellness creator | Enthusiastic, professional | "Your audience is ready — let's get it printed" |
| Food/recipe creator | Warm, visual, specific | "Cookbooks are our specialty — paper, binding, all of it" |
| Business/authority author | Professional, ROI-focused | "Your book is a business tool — let's make it excellent" |
| Social media creator | Casual, peer-level | "Your followers are asking for this — let's make it real" |
| Small press | Professional, partnership-focused | "Reliable manufacturing partner, one contact, no dropped details" |

---

## TECHNICAL NOTES FOR CLAUDE CODE

- **Email system:** SmarterMail via IMAP (Python `imaplib`)
- **IMAP host:** `mail.cushing-malloy.com` port 993 (SSL)
- **Outreach sender:** `printyourbook@cushing-malloy.com`
- **Drafts saved to:** Drafts folder — view at `https://mail.cushing-malloy.com`
- **Report recipient:** dylan@coxgp.com
- **Dashboard file location:** `/mnt/Dashboard/cushing-malloy-lead-dashboard.html`
- **Archive location:** `/mnt/Dashboard/02_Lead_Data/archive/`
- **Scheduled task:** Monday, 3:00 AM (weekly)
- **Python for PDF rebuild:** `python build_agent_overview.py` (if PDF needs updating)

---

*This document is confidential and proprietary to ideaBoss and Cushing-Malloy Books.*
*Version 2.3 | March 2026*
