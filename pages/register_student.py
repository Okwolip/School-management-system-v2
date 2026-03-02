import streamlit as st
from datetime import datetime
from database import supabase

st.title("Register Student")

SCHOOL_CODE = "ZFMA"

def generate_student_id():
    year = datetime.now().year

    # Get existing students
    response = supabase.table("students").select("student_id").execute()

    if not response.data:
        next_number = 1
    else:
        numbers = []

        for student in response.data:
            sid = student.get("student_id")
            if sid and sid.startswith(f"{SCHOOL_CODE}-{year}"):
                try:
                    number = int(sid.split("-")[-1])
                    numbers.append(number)
                except:
                    pass

        if numbers:
            next_number = max(numbers) + 1
        else:
            next_number = 1

    formatted_number = str(next_number).zfill(4)

    return f"{SCHOOL_CODE}-{year}-{formatted_number}"


student_name = st.text_input("Student Name")
dob = st.date_input("Date of Birth")
parent_name = st.text_input("Parent Name")
parent_phone = st.text_input("Parent Phone Number")

section = st.selectbox(
    "Section",
    ["Nursery", "Primary", "Secondary"]
)

session = st.selectbox(
    "Session",
    ["2025/2026", "2026/2027", "2027/2028"]
)

if st.button("Register Student"):
    if student_name == "":
        st.error("Student name is required")
    else:
        student_id = generate_student_id()

        data = {
            "student_id": student_id,
            "student_name": student_name,
            "date_of_birth": str(dob),
            "parent_name": parent_name,
            "parent_phone": parent_phone,
            "section": section,
            "session": session
        }

        response = supabase.table("students").insert(data).execute()

        if response.data:
            st.success(f"Student registered successfully. Student ID: {student_id}")
        else:
            st.error("Error registering student")
