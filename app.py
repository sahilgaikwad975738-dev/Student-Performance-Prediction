import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

st.title("Student Performance Prediction")

# Generate sample data if CSV doesn't exist
if not os.path.exists("student_data.csv"):
    sample_data = pd.DataFrame({
        'Study_Hours':    [7, 3, 5, 2, 8, 4, 6, 1, 9, 5],
        'Attendance':     [90, 60, 75, 40, 95, 65, 80, 30, 92, 70],
        'Previous_Score': [85, 50, 70, 45, 90, 60, 75, 35, 88, 65],
        'Result':         [1,  0,  1,  0,  1,  0,  1,  0,  1,  1]
    })
    sample_data.to_csv("student_data.csv", index=False)

# Load and train
data = pd.read_csv("student_data.csv")
X = data[['Study_Hours', 'Attendance', 'Previous_Score']]
y = data['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

st.success(f"Model Accuracy: {accuracy * 100:.2f}%")

st.subheader("Enter Student Details")
study_hours = st.slider("Study Hours per Day", 0, 12, 6)
attendance = st.slider("Attendance (%)", 0, 100, 85)
previous_score = st.slider("Previous Score", 0, 100, 78)

if st.button("Predict"):
    result = model.predict([[study_hours, attendance, previous_score]])
    if result[0] == 1:
        st.success("The student is likely to PASS")
    else:
        st.error("The student is likely to FAIL")
