import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("data/cleaned_college_data.csv")

# Define features and target variable
X = df[["CGPA", "Annual Family Income", "Faculty Count", "Total Students"]]
y = df["Placement Rate"]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save model and results
joblib.dump(model, "outputs/placement_model.pkl")
with open("outputs/model_performance.txt", "w") as f:
    f.write(f"MAE: {mae}\nR² Score: {r2}")
