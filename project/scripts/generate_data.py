"""
Generates a synthetic dataset structured after the well-known Kaggle
"Food Choices" (college student survey) dataset schema, for use in the
Tableau case study. Distributions are chosen to be plausible for a
sample of ~200 U.S. college students, based on published patterns from
the original survey and general college nutrition literature.
"""
import numpy as np
import pandas as pd

np.random.seed(42)
n = 200

genders = np.random.choice(["Female", "Male"], size=n, p=[0.62, 0.38])
years = np.random.choice(["Freshman", "Sophomore", "Junior", "Senior"], size=n, p=[0.28, 0.27, 0.24, 0.21])
on_off_campus = np.random.choice(["On-campus", "Off-campus"], size=n, p=[0.55, 0.45])
employment = np.random.choice(["Not employed", "Part-time", "Full-time"], size=n, p=[0.45, 0.45, 0.10])
income_bracket = np.random.choice(
    ["<$15,000", "$15,000-$29,999", "$30,000-$49,999", "$50,000-$74,999", "$75,000+"],
    size=n, p=[0.12, 0.18, 0.22, 0.24, 0.24]
)

gpa = np.clip(np.random.normal(3.3, 0.4, n), 2.0, 4.0).round(2)
exercise_freq = np.random.choice(["Never", "1-2x/week", "3-4x/week", "5+ x/week"], size=n, p=[0.14, 0.34, 0.32, 0.20])
sports_team = np.random.choice(["Yes", "No"], size=n, p=[0.22, 0.78])

fruit_day = np.random.choice([0, 1, 2, 3, 4], size=n, p=[0.10, 0.32, 0.30, 0.18, 0.10])
veggies_day = np.random.choice([0, 1, 2, 3, 4], size=n, p=[0.08, 0.30, 0.32, 0.20, 0.10])
eating_out_freq = np.random.choice(["Never", "1-2x/week", "3-5x/week", "6+ x/week"], size=n, p=[0.08, 0.42, 0.35, 0.15])
cook_freq = np.random.choice(["Never", "1-2x/week", "3-5x/week", "Daily"], size=n, p=[0.20, 0.32, 0.30, 0.18])
comfort_food_reason = np.random.choice(
    ["Stress", "Boredom", "Sadness", "Celebration/Happiness", "Laziness"],
    size=n, p=[0.34, 0.22, 0.16, 0.16, 0.12]
)
nutritional_check = np.random.choice(
    ["Never", "Rarely", "Sometimes", "Always"], size=n, p=[0.22, 0.30, 0.32, 0.16]
)
vitamins = np.random.choice(["Yes", "No"], size=n, p=[0.38, 0.62])
self_perception_weight = np.random.choice(
    ["Underweight", "About right", "Slightly overweight", "Overweight"],
    size=n, p=[0.09, 0.42, 0.32, 0.17]
)
life_rewarding = np.clip(np.random.normal(7.2, 1.6, n), 1, 10).round(0).astype(int)

# Weight/height to derive a simple BMI-ish number (synthetic, not diagnostic)
height_in = np.clip(np.random.normal(66, 4, n), 58, 78)
weight_lb = np.clip(np.random.normal(150, 30, n), 95, 260)
bmi = np.round((weight_lb / (height_in ** 2)) * 703, 1)

# Calorie estimates for 3 sample cafeteria items (mirrors original survey's
# "which food has more calories" comparison questions), used later for a
# nutrition literacy accuracy score
calorie_knowledge_correct = np.random.choice([0, 1, 2, 3], size=n, p=[0.18, 0.30, 0.32, 0.20])

df = pd.DataFrame({
    "student_id": np.arange(1, n + 1),
    "gender": genders,
    "class_year": years,
    "residence": on_off_campus,
    "employment_status": employment,
    "household_income": income_bracket,
    "gpa": gpa,
    "exercise_frequency": exercise_freq,
    "varsity_club_sports": sports_team,
    "fruit_servings_per_day": fruit_day,
    "veggie_servings_per_day": veggies_day,
    "eating_out_frequency": eating_out_freq,
    "home_cooking_frequency": cook_freq,
    "comfort_food_trigger": comfort_food_reason,
    "checks_nutrition_label": nutritional_check,
    "takes_vitamins": vitamins,
    "self_perceived_weight": self_perception_weight,
    "life_rewarding_score_1_10": life_rewarding,
    "height_in": height_in.round(1),
    "weight_lb": weight_lb.round(1),
    "bmi_est": bmi,
    "nutrition_calorie_quiz_correct_of_3": calorie_knowledge_correct,
})

df.to_csv("/home/claude/project/data/college_food_choices.csv", index=False)
print(df.shape)
print(df.head())
