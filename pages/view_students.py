import streamlit as st
import pandas as pd
from database import supabase

def show():
    st.title("All Students")

    response = supabase.table("students").select("*").execute()

    if response.data:
        df = pd.DataFrame(response.data)
        st.dataframe(df)

    role = st.session_state.user["role"]

    if role == "Admin":
        st.subheader("Delete Student")

        student_id = st.text_input("Student ID")
        student_name = st.text_input("Student Name")

        if st.button("Delete"):
            if student_id:
                supabase.table("students").delete().eq("student_id", student_id).execute()
                st.success("Student deleted")

            elif student_name:
                supabase.table("students").delete().eq("student_name", student_name).execute()
                st.success("Student deleted")
