from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT

OUTPUT = "/sessions/vigilant-dreamy-gauss/mnt/Dashboard/Cushing-Malloy-Agent-Overview.pdf"

# ── Colors
NAVY     = colors.HexColor("#1a2d45")
BLUE     = colors.HexColor("#3787c4")
BLUE_DK  = colors.HexColor("#2a6aa0")
MID      = colors.HexColor("#4a6080")
LGRAY    = colors.HexColor("#f0f3f7")
BORDER   = colors.HexColor("#d8e2ee")
WHITE    = colors.white
RED      = colors.HexColor("#d93a3a")
GREEN    = colors.HexColor("#1f9e5a")
AMBER    = colors.HexColor("#d08020")
TEAL     = colors.HexColor("#0e8a7a")

W = 7.6 * inch   # usable width

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.45*inch, rightMargin=0.45*inch,
    topMargin=0.3*inch,   bottomMargin=0.3*inch)

def ps(name, size=7, font="Helvetica", color=NAVY, leading=None, align=TA_LEFT, after=0, indent=0):
    return ParagraphStyle(name, fontSize=size, fontName=font, textColor=color,
                          leading=leading or size*1.35, alignment=align,
                          spaceAfter=after, leftIndent=indent)

sTitle   = ps("T",  16, "Helvetica-Bold", NAVY, 20)
sSub     = ps("Su",  8.5, color=BLUE,    leading=11.5)
sBand    = ps("Bn",  8.5, "Helvetica-Bold", WHITE, 11)
sHead    = ps("H",   8.5, "Helvetica-Bold", NAVY, 11)
sBody    = ps("Bo",  8,   color=MID,     leading=11,   align=TA_JUSTIFY)
sBul     = ps("Bu",  7.8, color=MID,     leading=10.5, indent=8, after=0)
sLabel   = ps("La",  7.5, "Helvetica-Bold", BLUE, 10)
sFoot    = ps("Fo",  7,   color=MID,     align=TA_CENTER)
sRed     = ps("Re",  7.8, "Helvetica-Bold", RED,  10.5)
sWt      = ps("Wt",  7.8, "Helvetica-Bold", BLUE, 10.5, align=TA_CENTER)
sCh      = ps("Ch",  7.5, color=MID,     leading=10.5, align=TA_JUSTIFY)
sChH     = ps("ChH", 8,   "Helvetica-Bold", NAVY, 10.5)

def band(text, bg=NAVY, w=W):
    t = Table([[Paragraph(text, sBand)]], colWidths=[w])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0),(-1,-1), bg),
        ("TOPPADDING",  (0,0),(-1,-1), 5), ("BOTTOMPADDING",(0,0),(-1,-1), 5),
        ("LEFTPADDING", (0,0),(-1,-1), 8), ("RIGHTPADDING", (0,0),(-1,-1), 8),
    ]))
    return t

def bul(text): return Paragraph(f"\u2022  {text}", sBul)
def sp(n=2):   return Spacer(1, n)

story = []

# ═══════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════
hdr = Table([[
    Paragraph("Cushing-Malloy Lead Intelligence Agent", sTitle),
    [Paragraph("AI Research Process — How It Works  ·  v2.0", sSub),
     Paragraph("ideaBoss for Cushing-Malloy Books  ·  March 2026  ·  CONFIDENTIAL",
               ps("sm", 6, color=MID))]
]], colWidths=[4.6*inch, 3.0*inch])
hdr.setStyle(TableStyle([
    ("VALIGN",         (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",     (0,0),(-1,-1), 8), ("BOTTOMPADDING",(0,0),(-1,-1), 7),
    ("LEFTPADDING",    (0,0),(0,-1),  8), ("RIGHTPADDING", (0,0),(0,-1),  8),
    ("LEFTPADDING",    (1,0),(1,-1),  6),
    ("BACKGROUND",     (0,0),(-1,-1), LGRAY),
    ("LINEBELOW",      (0,0),(-1,-1), 2, BLUE),
]))
story += [hdr, sp(8)]

# ═══════════════════════════════════════════════════════════════
# ROW 1: WHAT IT DOES  |  WHO IT TARGETS
# ═══════════════════════════════════════════════════════════════
LW, RW = 3.72*inch, 3.72*inch

left1 = [
    band("WHAT THIS AGENT DOES", NAVY, LW - 0.08*inch), sp(3),
    Paragraph("An AI prospecting agent that autonomously identifies, scores, and surfaces "
              "new sales leads for <b>Cushing-Malloy Books</b> — a family-owned book "
              "manufacturer in Ann Arbor, MI (est. 1948). It finds people who need books "
              "<b>physically printed</b>, not readers or book buyers.", sBody), sp(3),
    Paragraph("Each run the agent:", sHead), sp(1),
    bul("Generates 10–20 fresh, non-duplicate leads per run"),
    bul("Uses 4–5 distinct discovery channels per run"),
    bul("Scores every lead 1–10; surfaces only scores 5 and above"),
    bul("Writes a specific, actionable pitch angle for every lead"),
    bul("Sources the highest-quality leads across both individual authors/creators and small publishers"),
    bul("Spans multiple US states and regions each run"),
    sp(3),
    Paragraph("Why Cushing-Malloy?", sHead), sp(1),
    bul("Single point of contact — same person, start to finish"),
    bul("20 working days from approved files to finished books"),
    bul("White-glove guidance for first-time authors on every detail"),
    bul("Competitive at 250 copies; volume pricing education included"),
    bul("Offset AND digital printing + e-book conversion services"),
]

right1 = [
    band("WHO IT IS LOOKING FOR", BLUE_DK, RW - 0.08*inch), sp(3),
    Paragraph("<b>Audience A — Individual Authors &amp; Content Creators</b>", sHead),
    bul("First-time authors with manuscripts ready for a 250–5,000 copy run"),
    bul("Authors moving beyond POD platforms (KDP, IngramSpark, Lulu)"),
    bul("Health coaches, nutritionists, fitness &amp; wellness creators with a book"),
    bul("Recipe creators, food bloggers, and cookbook self-publishers"),
    bul("Business coaches and entrepreneurs publishing for authority/speaking"),
    bul("YouTube, Instagram, TikTok, podcast creators turning content into books"),
    bul("Substack writers with paid audiences announcing print projects"),
    bul("Kickstarter campaigns for book print runs"), sp(3),
    Paragraph("<b>Audience B — Small Independent Publishers</b>", sHead),
    bul("20 or fewer titles/year — micro and small press sweet spot"),
    bul("Not affiliated with Big 5 publishers or their imprints"),
    bul("Literary, regional, children's, poetry, and nonfiction specialty presses"),
    bul("IBPA members, Reedsy-listed, Poets &amp; Writers directory entries"),
    bul("Actively acquiring manuscripts or announcing upcoming titles"),
]

row1 = Table([[left1, right1]], colWidths=[LW, RW])
row1.setStyle(TableStyle([
    ("VALIGN", (0,0),(-1,-1), "TOP"),
    ("LEFTPADDING",(0,0),(0,-1), 0), ("RIGHTPADDING",(0,0),(0,-1), 6),
    ("LEFTPADDING",(1,0),(1,-1), 6), ("RIGHTPADDING",(1,0),(1,-1), 0),
    ("TOPPADDING",(0,0),(-1,-1),0), ("BOTTOMPADDING",(0,0),(-1,-1),0),
]))
story += [row1, sp(8)]

# ═══════════════════════════════════════════════════════════════
# ROW 2: DISCOVERY CHANNELS  (3 col × 2 row grid)
# ═══════════════════════════════════════════════════════════════
story += [band("HOW IT RESEARCHES — 20+ DISCOVERY CHANNELS ACROSS 6 CATEGORIES", BLUE_DK), sp(5)]

channels = [
    ("Creator & Social Channels",
     "Instagram/TikTok (\"book coming soon\"), YouTube channel book announcements, "
     "Substack authors with paid subscribers, podcast hosts writing books, "
     "Reddit: r/selfpublish, r/IndieAuthor, r/cookbookjunkies"),
    ("Publishing Platforms",
     "Amazon KDP Author Central, Goodreads author profiles (1–3 titles, recent dates), "
     "IngramSpark publisher accounts, BookBaby/Blurb/Lulu upgrade candidates, "
     "B&N Press, NaNoWriMo community graduates"),
    ("Crowdfunding & Events",
     "Kickstarter / Indiegogo book campaigns referencing offset print or bulk quantities; "
     "Eventbrite / bookstore author events; state arts council grant recipients "
     "(MI, OH, IL, WI, IN — production-ready funded projects)"),
    ("Industry Directories",
     "Poets & Writers Small Presses DB, IBPA member signals, Reedsy indie publisher "
     "directory, Bookshop.org indie storefronts, ALLi (Alliance of Independent Authors) members"),
    ("Trade & Professional",
     "LinkedIn (\"self-published author,\" \"book launch,\" \"writing my first book\"); "
     "Publishers Weekly Fast-Growing Indie list; Publishers Marketplace new imprints; "
     "Jane Friedman new imprint announcements"),
    ("Authority & Community",
     "Business/authority authors on Substack, health/wellness creator ecosystems, "
     "online course creators adding physical books; recipe bloggers announcing cookbooks; "
     "entrepreneur book launches via personal website or Kickstarter"),
]

cw = W / 3 - 2
ch_rows = []
for i in range(0, 6, 3):
    row = []
    for ch_name, ch_desc in channels[i:i+3]:
        cell = [Paragraph(ch_name, sChH), Paragraph(ch_desc, sCh)]
        row.append(cell)
    ch_rows.append(row)

ch_table = Table(ch_rows, colWidths=[cw, cw, cw])
ch_table.setStyle(TableStyle([
    ("VALIGN",        (0,0),(-1,-1), "TOP"),
    ("TOPPADDING",    (0,0),(-1,-1), 6), ("BOTTOMPADDING",(0,0),(-1,-1), 6),
    ("LEFTPADDING",   (0,0),(-1,-1), 7), ("RIGHTPADDING", (0,0),(-1,-1), 7),
    ("ROWBACKGROUNDS",(0,0),(-1,-1), [LGRAY, WHITE]),
    ("GRID",          (0,0),(-1,-1), 0.4, BORDER),
]))
story += [ch_table, sp(8)]

# ═══════════════════════════════════════════════════════════════
# ROW 3: SCORING  |  DATA FIELDS  |  GUARDRAILS
# ═══════════════════════════════════════════════════════════════
CW1, CW2, CW3 = 2.35*inch, 2.35*inch, 2.74*inch

# — Scoring Criteria (v2.0 weights)
score_items = [
    ("Print Volume Signal",     "25%"),
    ("Contact Completeness",    "20%"),
    ("Operational Activity",    "20%"),
    ("Audience & Reach",        "15%"),
    ("Geographic Reachability", "10%"),
    ("Growth Signal",            "5%"),
    ("Contact Quality",          "5%"),
]
sc_data = [[
    Paragraph(c, ps("scn", 7.5, "Helvetica-Bold", NAVY, 10)),
    Paragraph(w, ps("scw", 7.5, "Helvetica-Bold", BLUE, 10, align=TA_RIGHT)),
] for c, w in score_items]

sc_table = Table(sc_data, colWidths=[1.62*inch, 0.57*inch])
sc_table.setStyle(TableStyle([
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 4), ("BOTTOMPADDING",(0,0),(-1,-1), 4),
    ("LEFTPADDING",   (0,0),(-1,-1), 6), ("RIGHTPADDING", (0,0),(-1,-1), 6),
    ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, LGRAY]),
    ("LINEBELOW",     (0,0),(-1,-1), 0.4, BORDER),
    ("LINEABOVE",     (0,0),(-1, 0), 0.4, BORDER),
]))

# Tier badges
tier = Table([[
    Paragraph("9–10  HIGH", ps("th", 7, "Helvetica-Bold", WHITE, 9.5, TA_CENTER)),
    Paragraph("7–8  MEDIUM", ps("tm", 7, "Helvetica-Bold", NAVY, 9.5, TA_CENTER)),
    Paragraph("5–6  LOW", ps("tl", 7, "Helvetica-Bold", WHITE, 9.5, TA_CENTER)),
]], colWidths=[0.7*inch, 0.82*inch, 0.67*inch])
tier.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(0,-1), GREEN),
    ("BACKGROUND",    (1,0),(1,-1), colors.HexColor("#fdf0d0")),
    ("BACKGROUND",    (2,0),(2,-1), RED),
    ("TOPPADDING",    (0,0),(-1,-1), 4), ("BOTTOMPADDING",(0,0),(-1,-1), 4),
    ("LEFTPADDING",   (0,0),(-1,-1), 4), ("RIGHTPADDING", (0,0),(-1,-1), 4),
]))

col1 = [band("PRIORITY SCORING", GREEN, CW1), sp(2),
        Paragraph("Weighted formula — only leads scoring 5+ surfaced:", sBody), sp(2),
        sc_table, sp(3), tier]

# — Data Fields
fields = [
    ("Source",          "Discovery channel"),
    ("Company/Name",    "Publisher or author name"),
    ("Website",         "Confirmed primary URL"),
    ("Email",           "Verified or flagged not found"),
    ("Phone",           "Public listing if available"),
    ("Category",        "1 of 13 lead categories"),
    ("Priority Score",  "1–10 weighted score"),
    ("Pitch Notes",     "Specific outreach angle"),
]
fd_data = [[
    Paragraph(f, ps("fn", 7.5, "Helvetica-Bold", NAVY, 10)),
    Paragraph(d, ps("fd", 7.5, color=MID, leading=10)),
] for f, d in fields]
fd_table = Table(fd_data, colWidths=[1.1*inch, 1.09*inch])
fd_table.setStyle(TableStyle([
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 4), ("BOTTOMPADDING",(0,0),(-1,-1), 4),
    ("LEFTPADDING",   (0,0),(-1,-1), 6), ("RIGHTPADDING", (0,0),(-1,-1), 6),
    ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, LGRAY]),
    ("LINEBELOW",     (0,0),(-1,-1), 0.4, BORDER),
    ("LINEABOVE",     (0,0),(-1, 0), 0.4, BORDER),
]))
col2 = [band("DATA PER LEAD", BLUE, CW2), sp(2),
        Paragraph("8 fields collected for every lead:", sBody), sp(2), fd_table]

# — Guardrails
guards = [
    ("No fabricated leads",       "Every entity must be real and discoverable; contact info confirmed or flagged"),
    ("No POD platforms",          "KDP, IngramSpark, Lulu etc. are research tools, not prospects"),
    ("No Big 5 publishers",       "PRH, HarperCollins, S&S, Hachette, Macmillan and imprints excluded"),
    ("No print-irrelevant leads", "E-book-only / digital-only companies excluded"),
    ("No duplicate leads",        "All prior leads tracked; never repeated across sessions"),
    ("No generic pitches",        "Every Notes field must contain a specific, lead-specific outreach angle"),
    ("No niche domination",       "Academic & faith-based presses must not exceed 10% of any run"),
]
gd_data = [[
    Paragraph(g, sRed),
    Paragraph(d, ps("gd", 7.5, color=MID, leading=10.5)),
] for g, d in guards]
gd_table = Table(gd_data, colWidths=[1.2*inch, 1.38*inch])
gd_table.setStyle(TableStyle([
    ("VALIGN",        (0,0),(-1,-1), "TOP"),
    ("TOPPADDING",    (0,0),(-1,-1), 4), ("BOTTOMPADDING",(0,0),(-1,-1), 4),
    ("LEFTPADDING",   (0,0),(-1,-1), 6), ("RIGHTPADDING", (0,0),(-1,-1), 6),
    ("ROWBACKGROUNDS",(0,0),(-1,-1), [WHITE, colors.HexColor("#fff5f5")]),
    ("LINEBELOW",     (0,0),(-1,-1), 0.4, BORDER),
    ("LINEABOVE",     (0,0),(-1, 0), 0.4, BORDER),
]))
col3 = [band("QUALITY GUARDRAILS", RED, CW3), sp(2),
        Paragraph("What the agent will NEVER do:", sBody), sp(2), gd_table]

row3 = Table([[col1, col2, col3]], colWidths=[CW1, CW2, CW3])
row3.setStyle(TableStyle([
    ("VALIGN",       (0,0),(-1,-1), "TOP"),
    ("LEFTPADDING",  (0,0),(0,-1),  0), ("RIGHTPADDING",(0,0),(0,-1),  5),
    ("LEFTPADDING",  (1,0),(1,-1),  5), ("RIGHTPADDING",(1,0),(1,-1),  5),
    ("LEFTPADDING",  (2,0),(2,-1),  5), ("RIGHTPADDING",(2,0),(2,-1),  0),
    ("TOPPADDING",   (0,0),(-1,-1), 0), ("BOTTOMPADDING",(0,0),(-1,-1),0),
]))
story += [row3, sp(5)]

# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=3, spaceBefore=0))
story.append(Paragraph(
    "Cushing-Malloy Lead Intelligence Agent  ·  Powered by ideaBoss AI  ·  "
    "Version 2.0  ·  March 2026  ·  Confidential — ideaBoss for Cushing-Malloy Books",
    sFoot))

doc.build(story)
print("Done →", OUTPUT)
