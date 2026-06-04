import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

# Generate sample data if CSV doesn't exist
if not os.path.exists("student_data.csv"):
    sample_data = pd.DataFrame({
        'Study_Hours':    [7, 3, 5, 2, 8, 4, 6, 1, 9, 5],
        'Attendance':     [90, 60, 75, 40, 95, 65, 80, 30, 92, 70],
        'Previous_Score': [85, 50, 70, 45, 90, 60, 75, 35, 88, 65],
        'Result':         [1,  0,  1,  0,  1,  0,  1,  0,  1,  1]
    })
    sample_data.to_csv("student_data.csv", index=False)

# Load dataset
data = pd.read_csv("student_data.csv")

# Input and output
X = data[['Study_Hours', 'Attendance', 'Previous_Score']]
y = data['Result']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict new student
prediction = model.predict([[6, 85, 78]])

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")
