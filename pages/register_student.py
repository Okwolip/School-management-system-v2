import streamlit as st
from database import supabase

def show():
    st.title("Register Student")

    name = st.text_input("Student Name")
    dob = st.date_input("Date of Birth")
    parent_name = st.text_input("Parent Name")
    parent_phone = st.text_input("Parent Phone")

    section = st.selectbox("Section", ["Nursery", "Primary", "Secondary"])
    session = st.selectbox("Session", ["2025/2026", "2026/2027"])

    if st.button("Save Student"):
        data = {
            "student_name": name,
            "dob": str(dob),
            "parent_name": parent_name,
            "parent_phone": parent_phone,
            "section": section,
            "session": session
        }

        supabase.table("students").insert(data).execute()
        st.success("Student registered successfully")
