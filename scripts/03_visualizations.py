import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/cleaned_college_data.csv")

# Histogram of CGPA
plt.hist(df["CGPA"], bins=20, edgecolor="black")
plt.title("Distribution of CGPA")
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.savefig("outputs/cgpa_histogram.png")
plt.close()

# Scatter plot: CGPA vs Placement Rate
plt.scatter(df["CGPA"], df["Placement Rate"], alpha=0.5)
plt.title("CGPA vs Placement Rate")
plt.xlabel("CGPA")
plt.ylabel("Placement Rate")
plt.savefig("outputs/cgpa_vs_placement.png")
plt.close()
