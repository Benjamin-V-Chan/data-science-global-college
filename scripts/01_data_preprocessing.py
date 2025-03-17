import pandas as pd

# Load dataset
df = pd.read_csv("data/College Data.csv")

# Handle negative values in 'Female' column
df.loc[df["Female"] < 0, "Female"] = 0

# Fill missing values with appropriate strategies
df.fillna(df.median(numeric_only=True), inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_college_data.csv", index=False)
