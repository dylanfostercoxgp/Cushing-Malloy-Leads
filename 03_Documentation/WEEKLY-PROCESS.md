# Cushing-Malloy Lead Intelligence — Weekly Automation Process
**Client:** Cushing-Malloy Books | **Managed by:** ideaBoss | **Version:** 2.0 | **Updated:** March 2026

> **How to use this file:** Give this document to Claude (via Claude Code or Cowork mode) and say:
> *"Run the Cushing-Malloy weekly lead generation process."*
> Claude will follow every step in order, automatically.

---

## OVERVIEW

This process runs every **Monday at 3:00 AM** (or on-demand). It performs three jobs:

1. **Lead Discovery** — Research and score 10–20 new leads across multiple channels
2. **Outreach Drafts** — Create personalized Gmail draft emails to each verified lead (do NOT auto-send)
3. **Weekly Report** — Email a summary HTML report to dylan@coxgp.com

**Total estimated runtime:** 15–25 minutes depending on lead count.

---

## IDENTITY & CONTEXT

You are acting as a specialized lead generation intelligence agent for **Cushing-Malloy Books** (cushing-malloy.com), a third-generation, family-owned **book manufacturing and printing company** headquartered in Ann Arbor, Michigan. Founded in 1948. Ann Arbor is the "Short Run Book Capital of America."

You are finding people who need books **physically printed** — not book buyers, reviewers, or readers.

**Outreach signature to use in all emails:**
```
Warm regards,
Connie Cushing
Cushing-Malloy Books
(734) 663-8554
cushing-malloy.com
```

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
Orange Frazer Press, Bottom Dog Press, Fiddlehead Press, Porkbelly Press, Bex Kitchen, Idris Doosi, Paul Jarvis, Nat Eliason, Hill Schroder, Dickie Bush, Sohee Carpenter, M.G. Hunt, Sarah Styf, Rachel Moss, Erin Romeo

---

## STEP 2 — RESEARCH NEW LEADS

Using the full spec in `cushing-malloy-lead-gen-prompt.md`, research and identify **10–20 new leads**. Prioritize quality over category quotas — surface the best leads found, whether they are individual authors, content creators, or small publishers.

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
| **Phone** | If publicly listed; otherwise "Research Required" |
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

**RULE: Only surface leads scoring 5 or above. Discard leads below 5.**

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
    priority: "medium",         // "high" (9-10), "medium" (7-8), "low" (5-6)
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

5. Update the date selector options in the HTML `<select id="runSelect">` element to include the new date
6. Save the file to `Dashboard/cushing-malloy-lead-dashboard.html`
7. Also copy updated file to `Dashboard/01_Dashboard/cushing-malloy-lead-dashboard.html`

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

## STEP 5 — CREATE GMAIL OUTREACH DRAFTS

For every lead that has a **verified email address** (not "No Verified Email Found" or "Research Required"), create a personalized Gmail draft using the Gmail MCP tool.

**IMPORTANT: Save as DRAFT only. Do NOT send.**

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

Would a quick call this week work?

Warm regards,
Connie Cushing
Cushing-Malloy Books
(734) 663-8554
cushing-malloy.com
```

**Personalization checklist before creating each draft:**
- [ ] Subject line references their specific project
- [ ] Opening line shows you read their actual content/announcement
- [ ] Print run size estimate is realistic for their situation
- [ ] At least one differentiator is tailored to their specific need
- [ ] Tone matches their vibe (casual for creators, professional for publishers)

---

## STEP 6 — SEND WEEKLY REPORT EMAIL TO DYLAN

Create a Gmail draft (or send directly) to **dylan@coxgp.com** with the weekly summary report.

**Subject:** `Cushing-Malloy Lead Report — Week of [Monday Date]`

**Body (HTML formatted):**

```html
<p>Hi Dylan,</p>

<p>Here's your Cushing-Malloy lead generation report for the week of <strong>[DATE]</strong>.</p>

<h3>This Week's Summary</h3>
<ul>
  <li><strong>New leads researched:</strong> [X]</li>
  <li><strong>High priority (9–10):</strong> [X leads] — [names]</li>
  <li><strong>Medium priority (7–8):</strong> [X leads] — [names]</li>
  <li><strong>Low priority (5–6):</strong> [X leads] — [names]</li>
  <li><strong>Gmail outreach drafts created:</strong> [X] (ready to review and send)</li>
</ul>

<h3>Top 3 Leads This Week</h3>
<ol>
  <li><strong>[Name]</strong> — [Category] — Score [X]/10 — [1 sentence why]</li>
  <li><strong>[Name]</strong> — [Category] — Score [X]/10 — [1 sentence why]</li>
  <li><strong>[Name]</strong> — [Category] — Score [X]/10 — [1 sentence why]</li>
</ol>

<h3>Discovery Sources Used This Week</h3>
<p>[List the 4–5 channels used this run]</p>

<h3>Next Steps</h3>
<ul>
  <li>Review and send Gmail drafts for high-priority leads first</li>
  <li>Dashboard updated — view at [DASHBOARD URL when live]</li>
  <li>Next auto-run: Next Monday at 3:00 AM</li>
</ul>

<p>—ideaBoss AI Agent</p>
```

---

## STEP 7 — VERIFY COMPLETION

Run a final checklist before marking the process complete:

- [ ] 10–20 new leads researched and scored (all ≥ 5)
- [ ] Best leads surfaced regardless of category type
- [ ] At least 4–5 different discovery channels used
- [ ] Leads span multiple US states/regions
- [ ] No duplicates from previous runs
- [ ] Dashboard HTML updated with new run date and leads
- [ ] Lead archive JSON saved to `02_Lead_Data/archive/`
- [ ] Gmail outreach drafts created for all leads with verified emails
- [ ] Weekly report email drafted to dylan@coxgp.com
- [ ] Updated dashboard copied to `01_Dashboard/` folder

---

## FOLDER STRUCTURE REFERENCE

```
Dashboard/
├── cushing-malloy-lead-dashboard.html   ← MAIN DASHBOARD (edit this)
├── cushing-malloy-lead-gen-prompt.md    ← Full agent spec v2.0
├── WEEKLY-PROCESS.md                    ← This file
├── leads.json                           ← Reference/backup data
├── Cushing-Malloy-Agent-Overview.pdf    ← 1-page overview PDF
│
├── 01_Dashboard/
│   └── cushing-malloy-lead-dashboard.html   ← Copy of main dashboard
│
├── 02_Lead_Data/
│   └── archive/
│       └── leads-YYYY-MM-DD.json            ← Weekly lead snapshots
│
├── 03_Documentation/
│   ├── cushing-malloy-lead-gen-prompt.md
│   ├── Cushing-Malloy-Agent-Overview.pdf
│   └── WEEKLY-PROCESS.md
│
└── 04_Reports/
    └── (weekly HTML report archives, if saved)
```

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

- **Gmail MCP tool ID:** `mcp__5a941daf-9cda-4281-9985-37dacb85b091`
- **Gmail tool for creating drafts:** `gmail_create_draft`
- **Report recipient:** dylan@coxgp.com
- **Outreach sender:** dylan@coxgp.com (sends from Dylan's connected Gmail)
- **Dashboard file location:** `/mnt/Dashboard/cushing-malloy-lead-dashboard.html`
- **Archive location:** `/mnt/Dashboard/02_Lead_Data/archive/`
- **Scheduled task:** Monday, 3:00 AM (weekly)
- **Python for PDF rebuild:** `python build_agent_overview.py` (if PDF needs updating)

---

*This document is confidential and proprietary to ideaBoss and Cushing-Malloy Books.*
*Version 2.0 | March 2026*
