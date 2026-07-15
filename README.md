# Comprehensive Analysis and Dietary Strategies with Tableau
### A College Food Choices Case Study

A data analytics case study exploring how U.S. college students' eating habits, budgets, activity levels, and emotional states shape their dietary choices — built into a Tableau dashboard workflow with evidence-based recommendations for a campus wellness program.

## 📄 Full Report
See [`report/College_Food_Choices_Case_Study.pdf`](report/College_Food_Choices_Case_Study.pdf) for the complete write-up: executive summary, dataset description, step-by-step Tableau methodology, 8 visual analyses, and 6 actionable dietary strategies.

## 📊 Dataset
`data/college_food_choices.csv` — 200 student records, 22 fields (demographics, eating-out frequency, fruit/veggie intake, comfort-food triggers, exercise, GPA, nutrition literacy, self-perceived weight vs. BMI, supplement use).

Structured after the well-known Kaggle "Food Choices" college student survey. Swap this file for a real Kaggle export with matching column names to reproduce the analysis on genuine data — see [`scripts/generate_data.py`](scripts/generate_data.py) for the exact schema.

## 🗂️ Project Structure
```
├── data/
│   └── college_food_choices.csv       # Source dataset
├── images/
│   └── 01-08_*.png                    # Tableau-styled static charts
├── report/
│   └── College_Food_Choices_Case_Study.pdf   # Full case study document
├── scripts/
│   ├── generate_data.py               # Builds/refreshes the dataset
│   ├── make_charts.py                 # Generates the Tableau-styled charts
│   └── build_pdf.py                   # Assembles the PDF report
└── README.md
```

## 🛠️ How to Rebuild
```bash
pip install pandas numpy matplotlib reportlab
python scripts/generate_data.py   # -> data/college_food_choices.csv
python scripts/make_charts.py     # -> images/*.png
python scripts/build_pdf.py       # -> report/College_Food_Choices_Case_Study.pdf
```

## 📈 Rebuilding the Live Tableau Dashboard
1. Open Tableau Desktop/Public → **Connect → Text File** → select `data/college_food_choices.csv`.
2. Set `class_year`, `eating_out_frequency`, etc. as Dimensions; `gpa`, `bmi_est` as Measures.
3. Build one worksheet per question (see Section 3 of the PDF report for the full list).
4. Add filter/highlight dashboard actions to cross-filter all charts.
5. Combine into a Dashboard, then a Story with 3-4 narrative points.
6. Publish to Tableau Public / Server.

## 🔑 Key Findings
- 56% of students eat out 3+ times per week.
- 42% eat fewer than 2 fruit servings/day; 37.5% eat fewer than 2 veggie servings/day.
- Stress is the #1 comfort-food trigger (32%), ahead of boredom and celebration.
- Students exercising 3-4x/week average the highest GPA (3.44 vs. 3.25 for non-exercisers).
- Checking nutrition labels doesn't correlate with better calorie-knowledge quiz scores.
- 62% of students take no daily vitamin/supplement.

## License
MIT — feel free to fork and adapt for your own campus wellness case study.
