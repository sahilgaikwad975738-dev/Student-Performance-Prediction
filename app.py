import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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
