import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset and trained model
df = pd.read_csv("data/cleaned_college_data.csv")
model = joblib.load("outputs/placement_model.pkl")

# Define test set
X_test = df[["CGPA", "Annual Family Income", "Faculty Count", "Total Students"]]
y_test = df["Placement Rate"]

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save evaluation results
with open("outputs/final_results.txt", "w") as f:
    f.write(f"Final Model MAE: {mae}\nFinal R² Score: {r2}")
