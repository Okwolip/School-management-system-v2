import streamlit as st
from database import supabase
import uuid

def generate_student_id():
    return "STD-" + str(uuid.uuid4())[:8].upper()

def show():
    st.title("Register Student")

    name = st.text_input("Student Name")
    dob = st.date_input("Date of Birth")
    parent = st.text_input("Parent Name")
    phone = st.text_input("Parent Phone")

    section = st.selectbox("Section", ["Nursery", "Primary", "Secondary"])
    session = st.text_input("Session (e.g. 2025/2026)")

    if st.button("Register Student"):
        student_id = generate_student_id()

        data = {
            "student_id": student_id,
            "student_name": name,
            "dob": str(dob),
            "parent_name": parent,
            "parent_phone": phone,
            "section": section,
            "session": session
        }

        supabase.table("students").insert(data).execute()

        st.success(f"Student registered successfully. ID: {student_id}")
