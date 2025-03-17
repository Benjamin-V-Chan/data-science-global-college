import pandas as pd

# Load dataset
df = pd.read_csv("data/cleaned_college_data.csv")

# Summary statistics
summary_stats = df.describe()

# Correlation matrix
correlation_matrix = df.corr()

# Save results
summary_stats.to_csv("outputs/summary_statistics.csv")
correlation_matrix.to_csv("outputs/correlation_matrix.csv")
