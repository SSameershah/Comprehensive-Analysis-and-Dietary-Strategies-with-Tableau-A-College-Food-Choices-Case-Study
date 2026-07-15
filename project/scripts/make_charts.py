import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

df = pd.read_csv("/home/claude/project/data/college_food_choices.csv")

# Tableau 10 classic palette
TABLEAU = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
           "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC"]

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#5a5a5a",
    "axes.labelcolor": "#333333",
    "text.color": "#333333",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "axes.grid": True,
    "grid.color": "#e6e6e6",
    "grid.linewidth": 0.8,
    "axes.axisbelow": True,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

def style_ax(ax):
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#b0b0b0")
    ax.spines["bottom"].set_color("#b0b0b0")

# 1. Eating out frequency (bar)
fig, ax = plt.subplots(figsize=(7, 4.2))
order = ["Never", "1-2x/week", "3-5x/week", "6+ x/week"]
counts = df["eating_out_frequency"].value_counts().reindex(order)
bars = ax.bar(counts.index, counts.values, color=TABLEAU[0], width=0.6)
for b in bars:
    ax.annotate(f"{int(b.get_height())}", (b.get_x()+b.get_width()/2, b.get_height()),
                ha="center", va="bottom", fontsize=9)
ax.set_title("How Often Students Eat Out", fontsize=13, weight="bold", loc="left")
ax.set_ylabel("Number of students")
style_ax(ax)
plt.tight_layout()
plt.savefig("/home/claude/project/images/01_eating_out_frequency.png", dpi=180)
plt.close()

# 2. Fruit & Veggie servings comparison (grouped bar)
fig, ax = plt.subplots(figsize=(7, 4.2))
fruit_counts = df["fruit_servings_per_day"].value_counts().sort_index()
veg_counts = df["veggie_servings_per_day"].value_counts().sort_index()
x = np.arange(5)
width = 0.35
ax.bar(x - width/2, fruit_counts.reindex(range(5), fill_value=0), width, label="Fruit", color=TABLEAU[4])
ax.bar(x + width/2, veg_counts.reindex(range(5), fill_value=0), width, label="Vegetables", color=TABLEAU[1])
ax.set_xticks(x)
ax.set_xticklabels(["0", "1", "2", "3", "4+"])
ax.set_xlabel("Servings per day")
ax.set_ylabel("Number of students")
ax.set_title("Daily Fruit & Vegetable Servings", fontsize=13, weight="bold", loc="left")
ax.legend(frameon=False)
style_ax(ax)
plt.tight_layout()
plt.savefig("/home/claude/project/images/02_fruit_veggie_servings.png", dpi=180)
plt.close()

# 3. Comfort food emotional triggers (horizontal bar, sorted)
fig, ax = plt.subplots(figsize=(7, 4.2))
cf = df["comfort_food_trigger"].value_counts().sort_values()
ax.barh(cf.index, cf.values, color=TABLEAU[2])
for i, v in enumerate(cf.values):
    ax.annotate(str(v), (v, i), va="center", ha="left", fontsize=9, xytext=(4,0), textcoords="offset points")
ax.set_title("What Triggers Comfort-Food Eating", fontsize=13, weight="bold", loc="left")
ax.set_xlabel("Number of students")
style_ax(ax)
plt.tight_layout()
plt.savefig("/home/claude/project/images/03_comfort_food_triggers.png", dpi=180)
plt.close()

# 4. GPA vs exercise frequency (box-style using bar of means + error)
fig, ax = plt.subplots(figsize=(7, 4.2))
order_ex = ["Never", "1-2x/week", "3-4x/week", "5+ x/week"]
grp = df.groupby("exercise_frequency")["gpa"].agg(["mean", "std"]).reindex(order_ex)
ax.bar(grp.index, grp["mean"], yerr=grp["std"], capsize=4, color=TABLEAU[3])
ax.set_ylim(2.5, 4.0)
ax.set_ylabel("Average GPA")
ax.set_title("Average GPA by Exercise Frequency", fontsize=13, weight="bold", loc="left")
style_ax(ax)
plt.tight_layout()
plt.savefig("/home/claude/project/images/04_gpa_vs_exercise.png", dpi=180)
plt.close()

# 5. Self-perceived weight vs BMI estimate (scatter/box hybrid: boxplot)
fig, ax = plt.subplots(figsize=(7, 4.2))
order_w = ["Underweight", "About right", "Slightly overweight", "Overweight"]
data_by_cat = [df.loc[df["self_perceived_weight"] == cat, "bmi_est"].values for cat in order_w]
bp = ax.boxplot(data_by_cat, labels=order_w, patch_artist=True, widths=0.55)
for patch, color in zip(bp["boxes"], TABLEAU[:4]):
    patch.set_facecolor(color)
    patch.set_alpha(0.75)
for element in ["whiskers", "caps", "medians"]:
    for line in bp[element]:
        line.set_color("#4d4d4d")
ax.set_ylabel("Estimated BMI")
ax.set_title("Self-Perceived Weight vs. Estimated BMI", fontsize=13, weight="bold", loc="left")
style_ax(ax)
plt.tight_layout()
plt.savefig("/home/claude/project/images/05_selfperception_vs_bmi.png", dpi=180)
plt.close()

# 6. Nutrition label checking vs calorie quiz score (heatmap-style bar)
fig, ax = plt.subplots(figsize=(7, 4.2))
order_n = ["Never", "Rarely", "Sometimes", "Always"]
grp2 = df.groupby("checks_nutrition_label")["nutrition_calorie_quiz_correct_of_3"].mean().reindex(order_n)
bars = ax.bar(grp2.index, grp2.values, color=TABLEAU[5])
ax.set_ylim(0, 3)
ax.set_ylabel("Avg. correct answers (of 3)")
ax.set_title("Nutrition Label Checking vs. Calorie Knowledge", fontsize=13, weight="bold", loc="left")
for b in bars:
    ax.annotate(f"{b.get_height():.1f}", (b.get_x()+b.get_width()/2, b.get_height()),
                ha="center", va="bottom", fontsize=9)
style_ax(ax)
plt.tight_layout()
plt.savefig("/home/claude/project/images/06_label_checking_vs_knowledge.png", dpi=180)
plt.close()

# 7. Income bracket vs eating-out frequency (stacked bar, % within income)
fig, ax = plt.subplots(figsize=(7.5, 4.5))
order_i = ["<$15,000", "$15,000-$29,999", "$30,000-$49,999", "$50,000-$74,999", "$75,000+"]
ct = pd.crosstab(df["household_income"], df["eating_out_frequency"], normalize="index").reindex(order_i)[order]
bottom = np.zeros(len(ct))
for i, col in enumerate(order):
    ax.bar(ct.index, ct[col]*100, bottom=bottom, label=col, color=TABLEAU[i])
    bottom += ct[col].values*100
ax.set_ylabel("% of students")
ax.set_title("Eating-Out Frequency by Household Income", fontsize=13, weight="bold", loc="left")
plt.setp(ax.get_xticklabels(), rotation=20, ha="right")
ax.legend(frameon=False, bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
style_ax(ax)
plt.tight_layout()
plt.savefig("/home/claude/project/images/07_income_vs_eatingout.png", dpi=180)
plt.close()

# 8. Vitamins usage donut
fig, ax = plt.subplots(figsize=(5.5, 5.5))
vit = df["takes_vitamins"].value_counts()
wedges, texts, autotexts = ax.pie(
    vit.values, labels=vit.index, autopct="%1.0f%%", startangle=90,
    colors=[TABLEAU[0], TABLEAU[8]], wedgeprops=dict(width=0.4, edgecolor="white")
)
ax.set_title("Do Students Take Daily Vitamins?", fontsize=13, weight="bold")
plt.tight_layout()
plt.savefig("/home/claude/project/images/08_vitamins_donut.png", dpi=180)
plt.close()

print("Charts created:")
import os
for f in sorted(os.listdir("/home/claude/project/images")):
    print(" -", f)
