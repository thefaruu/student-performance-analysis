
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "student_performance.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

print("First five rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nSummary statistics:")
print(df.describe().round(2))

# Average subject scores
score_columns = ["math_score", "economics_score"]

print("\nAverage scores:")
print(df[score_columns].mean().round(2))

# Students scoring at least 40 in both subjects
pass_rate = (df[score_columns] >= 40).all(axis=1).mean() * 100
print(f"\nPass rate: {pass_rate:.1f}%")

# Study hours and maths score correlation
correlation = df["study_hours_per_week"].corr(df["math_score"])
print(f"Study hours vs maths score correlation: {correlation:.2f}")

# Score distribution chart
df[score_columns].plot(
    kind="hist",
    bins=10,
    alpha=0.65,
    edgecolor="black"
)

plt.title("Distribution of Student Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "score_distribution.png")
plt.close()

# Study hours vs maths score chart
plt.figure(figsize=(7, 5))
plt.scatter(
    df["study_hours_per_week"],
    df["math_score"],
    alpha=0.75
)

plt.title("Weekly Study Hours vs Maths Score")
plt.xlabel("Study Hours Per Week")
plt.ylabel("Maths Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "study_hours_vs_math_score.png")
plt.close()

print("\nAnalysis completed successfully!")
