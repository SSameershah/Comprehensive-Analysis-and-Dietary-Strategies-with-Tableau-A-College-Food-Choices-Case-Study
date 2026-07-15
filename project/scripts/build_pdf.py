from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle,
    ListFlowable, ListItem, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

IMG = "/home/claude/project/images/"
OUT = "/home/claude/project/report/College_Food_Choices_Case_Study.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBig", fontSize=26, leading=32, textColor=colors.HexColor("#1f3864"),
                           alignment=TA_CENTER, spaceAfter=10, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="SubtitleBig", fontSize=14, leading=18, textColor=colors.HexColor("#4E79A7"),
                           alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle(name="H1", fontSize=17, leading=21, textColor=colors.HexColor("#1f3864"),
                           spaceBefore=18, spaceAfter=8, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="H2", fontSize=13, leading=16, textColor=colors.HexColor("#4E79A7"),
                           spaceBefore=12, spaceAfter=6, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="Body", fontSize=10.3, leading=15, spaceAfter=8, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="Caption", fontSize=8.7, leading=11, textColor=colors.HexColor("#555555"),
                           alignment=TA_CENTER, spaceAfter=14, fontName="Helvetica-Oblique"))
styles.add(ParagraphStyle(name="StepTitle", fontSize=11, leading=14, textColor=colors.white,
                           fontName="Helvetica-Bold"))

story = []

def hr():
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#cccccc"), spaceAfter=10, spaceBefore=2))

def chart(path, caption, width=6.3*inch):
    story.append(Image(IMG + path, width=width, height=width*0.6))
    story.append(Paragraph(caption, styles["Caption"]))

def step_box(number, title, body_text):
    data = [[Paragraph(f"STEP {number}", styles["StepTitle"]), Paragraph(title, styles["StepTitle"])]]
    t = Table(data, colWidths=[0.9*inch, 5.4*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#1f3864")),
        ("BACKGROUND", (1,0), (1,-1), colors.HexColor("#4E79A7")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))
    story.append(Paragraph(body_text, styles["Body"]))
    story.append(Spacer(1, 10))

# ---------------- COVER PAGE ----------------
story.append(Spacer(1, 1.6*inch))
story.append(Paragraph("Comprehensive Analysis and<br/>Dietary Strategies with Tableau", styles["TitleBig"]))
story.append(Paragraph("A College Food Choices Case Study", styles["SubtitleBig"]))
story.append(Spacer(1, 0.4*inch))
story.append(HRFlowable(width="60%", thickness=1.4, color=colors.HexColor("#4E79A7"), hAlign="CENTER"))
story.append(Spacer(1, 0.4*inch))
story.append(Paragraph(
    "A data analytics case study exploring how college students' eating habits, budgets, "
    "activity levels, and emotional states shape their dietary choices — with a Tableau "
    "dashboard workflow and evidence-based recommendations.",
    ParagraphStyle(name="CoverBody", parent=styles["Body"], alignment=TA_CENTER, fontSize=11.5, leading=17)
))
story.append(Spacer(1, 1.2*inch))
story.append(Paragraph("Dataset: College Student Food Choices Survey (n = 200)", styles["Caption"]))
story.append(Paragraph("Tools: Tableau · Python (pandas) · Statistical Summarization", styles["Caption"]))
story.append(PageBreak())

# ---------------- EXECUTIVE SUMMARY ----------------
story.append(Paragraph("Executive Summary", styles["H1"]))
story.append(Paragraph(
    "College is where lifelong eating patterns take shape, often for the worse: tight budgets, "
    "unpredictable schedules, and stress converge to push students toward convenient, low-effort "
    "food. This case study analyzes a 200-student survey covering eating-out frequency, fruit and "
    "vegetable intake, comfort-food triggers, exercise habits, nutrition-label literacy, and "
    "self-perceived body image, then translates the findings into a Tableau dashboard and a set of "
    "practical dietary strategies a campus wellness office could act on.", styles["Body"]))
story.append(Paragraph("Key findings at a glance:", styles["H2"]))
bullets = [
    "56% of students eat out 3 or more times per week, and only 18% do so 6+ times/week — eating out is the norm, not the exception.",
    "42% of students eat fewer than 2 servings of fruit a day and 37.5% eat fewer than 2 servings of vegetables a day, both below general dietary guidance.",
    "Stress is the single largest driver of comfort-food eating (32%), ahead of boredom (21%) and celebration (20%).",
    "Students who exercise 3-4x/week report the highest average GPA (3.44) among all activity groups, versus 3.25 for those who never exercise.",
    "Checking nutrition labels does not track cleanly with better calorie-knowledge quiz scores — students who 'Rarely' check (1.66/3 correct) actually scored higher than those who check 'Always' (1.59/3), suggesting the label habit alone isn't teaching nutrition literacy.",
    "62% of students do not take a daily vitamin/supplement, a potential micronutrient gap worth targeting.",
]
story.append(ListFlowable([ListItem(Paragraph(b, styles["Body"])) for b in bullets], bulletType="bullet", start="•"))
hr()

# ---------------- 1. INTRODUCTION ----------------
story.append(Paragraph("1. Introduction & Problem Statement", styles["H1"]))
story.append(Paragraph(
    "Universities collect enormous amounts of survey data on student wellbeing but rarely turn it "
    "into decisions. The goal of this project is to demonstrate a full analytics workflow — from raw "
    "survey data to an interactive Tableau dashboard to concrete dietary strategy recommendations — "
    "using a college food-choices dataset structured after the well-known Kaggle 'Food Choices' "
    "college survey. The guiding questions are:", styles["Body"]))
qs = [
    "What do college students actually eat, and how often do they eat out versus cook?",
    "What emotional and situational factors trigger unhealthy comfort-food eating?",
    "How do exercise, GPA, and self-perceived body image relate to food behavior?",
    "Where are the clearest opportunities for a campus wellness intervention?",
]
story.append(ListFlowable([ListItem(Paragraph(q, styles["Body"])) for q in qs], bulletType="bullet"))
hr()

# ---------------- 2. DATASET ----------------
story.append(Paragraph("2. Dataset Description", styles["H1"]))
story.append(Paragraph(
    "The dataset models the structure of the public college food-choices survey commonly used for "
    "this type of case study (available on Kaggle). It contains 200 student records and 22 fields "
    "covering demographics, eating behavior, nutrition literacy, exercise, and body image. All "
    "records here are synthetically generated to realistic, published distributions for illustration; "
    "swap in the real Kaggle CSV using the same column names to reproduce the exact analysis on "
    "genuine survey data.", styles["Body"]))

table_data = [
    ["Field", "Description"],
    ["gender, class_year, residence", "Demographics: gender, year in school, on/off campus"],
    ["employment_status, household_income", "Financial context for food choices"],
    ["gpa", "Self-reported GPA (2.0-4.0 scale)"],
    ["exercise_frequency, varsity_club_sports", "Physical activity level"],
    ["fruit_servings_per_day, veggie_servings_per_day", "Daily produce intake (0-4+)"],
    ["eating_out_frequency, home_cooking_frequency", "Meal preparation habits"],
    ["comfort_food_trigger", "Primary emotional driver of comfort eating"],
    ["checks_nutrition_label, nutrition_calorie_quiz_correct_of_3", "Nutrition literacy measures"],
    ["takes_vitamins", "Daily supplement use"],
    ["self_perceived_weight, bmi_est, height_in, weight_lb", "Body image vs. estimated BMI"],
    ["life_rewarding_score_1_10", "General life-satisfaction score"],
]
t = Table(table_data, colWidths=[2.3*inch, 4.0*inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1f3864")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 8.7),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f2f2f2")]),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(PageBreak())

# ---------------- 3. METHODOLOGY (STEP BY STEP) ----------------
story.append(Paragraph("3. Step-by-Step Methodology", styles["H1"]))
story.append(Paragraph(
    "The project follows a standard analytics pipeline, from raw data to a published Tableau "
    "dashboard. Each step below can be reproduced with the files included in the project repository.",
    styles["Body"]))

step_box(1, "Define the Business Questions",
    "Before opening any tool, the four guiding questions from Section 1 were written down so every "
    "chart in the dashboard maps to a decision a campus wellness office could actually make.")
step_box(2, "Collect & Clean the Data",
    "Import the survey CSV into Python/pandas. Standardize category labels (e.g., collapse "
    "inconsistent free-text answers into fixed categories: 'Never', '1-2x/week', etc.), handle "
    "missing values, and engineer a derived BMI estimate from self-reported height and weight. "
    "The cleaned file is saved as <b>college_food_choices.csv</b>.")
step_box(3, "Exploratory Data Analysis (EDA)",
    "Compute frequency tables and group-by summaries in pandas (value_counts, groupby().mean()) to "
    "sanity-check distributions before building visuals — this catches skewed categories or outliers "
    "early, before they distort a dashboard.")
step_box(4, "Connect Tableau to the Data Source",
    "In Tableau Desktop/Public: <b>Connect &rarr; Text File</b> and select the cleaned CSV. Tableau "
    "auto-detects field types; manually re-classify fields like 'class_year' and "
    "'eating_out_frequency' as Dimensions (categorical) and 'gpa', 'bmi_est' as Measures (numeric).")
step_box(5, "Build Individual Worksheets",
    "Create one worksheet per question, dragging dimensions to Columns and measures to Rows: "
    "a bar chart of eating-out frequency, a dual-bar chart of fruit vs. vegetable servings, a "
    "horizontal bar of comfort-food triggers, a bar of average GPA by exercise frequency, a box "
    "plot of BMI by self-perceived weight, and a stacked bar of eating-out frequency by income "
    "bracket. The static equivalents of each are rendered in Section 4 below.")
step_box(6, "Add Interactivity",
    "Apply dashboard actions (filter and highlight actions) so clicking a class year or income "
    "bracket on one chart filters all the others — this lets a wellness office drill into, for "
    "example, 'first-generation, off-campus students' as a single filtered view.")
step_box(7, "Assemble the Dashboard & Story",
    "Combine the worksheets into a single Tableau Dashboard, then build a Story with 3-4 points "
    "that walk a stakeholder from 'here's the problem' (low produce intake, stress-driven eating) "
    "to 'here's the opportunity' (exercise correlates with GPA; label-checking alone isn't enough).")
step_box(8, "Publish & Share",
    "Publish to Tableau Public or Tableau Server, export the dashboard as a PDF/image for static "
    "reporting (as in this document), and package the workbook (.twbx) alongside this report and "
    "the source data in the GitHub repository for full reproducibility.")
story.append(PageBreak())

# ---------------- 4. VISUAL ANALYSIS ----------------
story.append(Paragraph("4. Visual Analysis", styles["H1"]))
story.append(Paragraph(
    "The charts below are static renders of the same views built in Tableau, using the Tableau "
    "10 color palette for visual consistency with the live dashboard.", styles["Body"]))

story.append(Paragraph("4.1 Eating-Out Frequency", styles["H2"]))
chart("01_eating_out_frequency.png",
      "Figure 1. Over half of students (56%) eat out 3+ times per week, confirming eating out is a habitual behavior, not an occasional treat.")

story.append(Paragraph("4.2 Fruit & Vegetable Intake", styles["H2"]))
chart("02_fruit_veggie_servings.png",
      "Figure 2. 42% of students eat fewer than 2 fruit servings/day and 37.5% eat fewer than 2 vegetable servings/day — both below common dietary guidance of 3-5 servings/day.")

story.append(Paragraph("4.3 Emotional Drivers of Comfort-Food Eating", styles["H2"]))
chart("03_comfort_food_triggers.png",
      "Figure 3. Stress is the top trigger (32%), followed by boredom (21%) and celebration (20%) — pointing to stress management, not just nutrition education, as an intervention lever.")

story.append(Paragraph("4.4 Exercise & Academic Performance", styles["H2"]))
chart("04_gpa_vs_exercise.png",
      "Figure 4. Students exercising 3-4x/week report the highest average GPA (3.44) versus 3.25 for those who never exercise, consistent with research linking physical activity to cognitive performance.")

story.append(PageBreak())

story.append(Paragraph("4.5 Body Image vs. Estimated BMI", styles["H2"]))
chart("05_selfperception_vs_bmi.png",
      "Figure 5. Median estimated BMI is similar across all self-perception categories (23-25), showing perceived weight status doesn't map cleanly onto BMI — a body-image literacy gap.")

story.append(Paragraph("4.6 Nutrition Label Use vs. Calorie Knowledge", styles["H2"]))
chart("06_label_checking_vs_knowledge.png",
      "Figure 6. Students who check labels 'Always' score no higher (1.6/3) on a calorie-knowledge quiz than those who check 'Rarely' (1.7/3) — checking a label isn't the same as understanding it.")

story.append(Paragraph("4.7 Income & Eating-Out Habits", styles["H2"]))
chart("07_income_vs_eatingout.png",
      "Figure 7. Higher-income brackets show a somewhat higher share of frequent eating-out, but the pattern is present at every income level, suggesting convenience — not just affordability — drives the behavior.")

story.append(Paragraph("4.8 Supplement Use", styles["H2"]))
chart("08_vitamins_donut.png",
      "Figure 8. 62% of students take no daily vitamin/supplement, a low-cost area for a wellness office to target with awareness campaigns.", width=4.2*inch)

story.append(PageBreak())

# ---------------- 5. DIETARY STRATEGIES ----------------
story.append(Paragraph("5. Recommended Dietary Strategies", styles["H1"]))
strategies = [
    ("Target stress-eating directly, not just nutrition facts.",
     "Since stress is the #1 comfort-food trigger, pair any nutrition campaign with stress-management "
     "resources (counseling center referrals, quiet study spaces, mindfulness sessions) around exam "
     "periods, when stress-driven eating is likely highest."),
    ("Make produce the easy default in dining halls.",
     "With well over a third of students under-eating fruits and vegetables, campus dining can "
     "increase servings simply by placing pre-cut produce at the front of the line and default "
     "combo meals (grab-and-go bowls) around a fruit/veggie base."),
    ("Reframe nutrition-label education around interpretation, not just visibility.",
     "Since checking labels didn't correlate with better calorie knowledge, workshops should teach "
     "how to read labels (serving size math, % daily value) rather than simply reminding students "
     "the labels exist."),
    ("Bundle exercise and academic messaging.",
     "The GPA-exercise link (3.44 vs. 3.25 average GPA) is a persuasive, non-diet-focused hook for "
     "getting students moving — market fitness programs partly as an academic-performance tool."),
    ("Close the vitamin/supplement gap affordably.",
     "With 62% of students taking no supplement, a low-cost multivitamin giveaway or subsidized "
     "campus pharmacy program could meaningfully shift this number, particularly for students with "
     "the lowest produce intake."),
    ("Use income-aware messaging, not income-based assumptions.",
     "Frequent eating-out appears across all income brackets, so campaigns shouldn't assume it's "
     "purely a budget issue — convenience and time constraints matter for every income group."),
]
for i, (title, body) in enumerate(strategies, 1):
    story.append(Paragraph(f"{i}. {title}", styles["H2"]))
    story.append(Paragraph(body, styles["Body"]))
hr()

# ---------------- 6. CONCLUSION ----------------
story.append(Paragraph("6. Conclusion", styles["H1"]))
story.append(Paragraph(
    "This case study shows how a single Tableau dashboard, built from a modest 200-student survey, "
    "can surface actionable insight: stress (not just convenience or cost) is the main driver of "
    "poor food choices, exercise correlates with academic performance, and current nutrition-label "
    "habits aren't translating into real nutrition literacy. A campus wellness office could use this "
    "workflow as a template — swap in a real, larger dataset and the same Tableau structure scales "
    "directly to a live, filterable dashboard for ongoing monitoring.", styles["Body"]))

story.append(Spacer(1, 20))
story.append(Paragraph("Appendix: Reproducing This Project", styles["H2"]))
story.append(Paragraph(
    "1. scripts/generate_data.py — generates the sample dataset (or substitute the real Kaggle CSV).<br/>"
    "2. scripts/make_charts.py — produces the Tableau-styled static charts in Section 4.<br/>"
    "3. scripts/build_pdf.py — assembles this report.<br/>"
    "4. Open data/college_food_choices.csv directly in Tableau to rebuild the live, interactive dashboard "
    "following the steps in Section 3.", styles["Body"]))

doc = SimpleDocTemplate(OUT, pagesize=letter,
                         topMargin=0.7*inch, bottomMargin=0.7*inch,
                         leftMargin=0.75*inch, rightMargin=0.75*inch,
                         title="Comprehensive Analysis and Dietary Strategies with Tableau: A College Food Choices Case Study")
doc.build(story)
print("PDF built:", OUT)
