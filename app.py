import streamlit as st

st.title("Student Result")

name = st.text_input("Student Name")
maths = st.number_input("Maths", 0, 100)
science = st.number_input("Science", 0, 100)
english = st.number_input("English", 0, 100)

if st.button("Predict"):
    percentage = (maths + science + english) / 3
    grade = "A" if percentage >= 80 else "B" if percentage >= 60 else "C" if percentage >= 40 else "F"

    st.write(f"**Name:** {name}")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")

    if percentage >= 40:
        st.success("PASS")
    else:
        st.error("FAIL")
