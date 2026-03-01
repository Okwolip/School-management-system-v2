import streamlit as st
from database import supabase
import uuid

def generate_student_id():
    return "STD-" + str(uuid.uuid4())[:8].upper()

def show():
    st.title("Register Student")

    student_name = st.text_input("Student Name")
    dob = st.date_input("Date of Birth")
    parent_name = st.text_input("Parent Name")
    parent_phone = st.text_input("Parent Phone")

    section = st.selectbox("Section", ["Nursery", "Primary", "Secondary"])
    session = st.selectbox("Session", ["2025/2026", "2026/2027"])

    if st.button("Register Student"):

        student_id = generate_student_id()

        data = {
            "student_id": student_id,
            "student_name": student_name,
            "dob": str(dob),
            "parent_name": parent_name,
            "parent_phone": parent_phone,
            "section": section,
            "session": session
        }

        supabase.table("students").insert(data).execute()

        st.success(f"Student registered successfully. ID: {student_id}")
