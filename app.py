import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Train model from CSV
data = pd.read_csv("student_data.csv")
X = data[['Study_Hours', 'Attendance', 'Previous_Score']]
y = data['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

st.title("🎓 Student Result Predictor")

name         = st.text_input("Student Name")
study_hours  = st.number_input("Study Hours", 0, 24)
attendance   = st.number_input("Attendance (%)", 0, 100)
prev_score   = st.number_input("Previous Score", 0, 100)

if st.button("Predict"):
    percentage = (attendance + prev_score) / 2
    grade = "A" if percentage >= 80 else "B" if percentage >= 60 else "C" if percentage >= 40 else "F"
    result = model.predict([[study_hours, attendance, prev_score]])[0]

    st.write(f"**Name:** {name}")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")

    if result == 1:
        st.success("✅ PASS")
    else:
        st.error("❌ FAIL")
