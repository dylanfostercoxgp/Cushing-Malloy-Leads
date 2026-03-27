# Cushing-Malloy Lead Intelligence System

AI-powered lead generation for **Cushing-Malloy Books** — Ann Arbor, MI (est. 1948).

Managed by **ideaBoss** | Client contact: Connie Cushing | Report to: dylan@coxgp.com

---

## What This Is

An automated weekly lead generation system that:
- Researches 10–20 new leads per run across authors, content creators, and small publishers
- Scores every lead 1–10 using a weighted formula
- Creates personalized Gmail draft outreach for every verified email
- Sends a weekly summary report to Dylan
- Updates the interactive lead dashboard

**Runs automatically every Monday at 3:00 AM.**

---

## Folder Structure

```
├── 01_Dashboard/
│   └── cushing-malloy-lead-dashboard.html   ← Interactive lead dashboard
├── 02_Lead_Data/
│   └── archive/                             ← Weekly lead JSON snapshots
├── 03_Documentation/
│   ├── cushing-malloy-lead-gen-prompt.md    ← Full agent spec v2.0
│   ├── Cushing-Malloy-Agent-Overview.pdf    ← 1-page agent overview
│   ├── CushingMalloy_StyleGuide.docx        ← Brand style guide
│   └── WEEKLY-PROCESS.md                   ← Step-by-step process doc
├── 04_Reports/                              ← Weekly report archives
├── build_agent_overview.py                  ← ReportLab PDF generator script
├── Cushing-Malloy-Agent-Overview.pdf        ← 1-page agent overview (root copy)
└── WEEKLY-PROCESS.md                        ← Process doc (root copy)
```

---

## Running the Weekly Process Manually

Open Cowork or Claude Code and say:
> "Run the Cushing-Malloy weekly lead generation process."

Then point Claude to `WEEKLY-PROCESS.md` — it contains every step.

---

*Confidential — ideaBoss for Cushing-Malloy Books*
