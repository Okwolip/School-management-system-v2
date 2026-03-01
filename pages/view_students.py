import streamlit as st
import pandas as pd
from database import supabase

def show():
    st.title("All Students")

    response = supabase.table("students").select("*").execute()
    data = response.data

    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)

    st.divider()
    st.subheader("Admin: Delete Student")

    role = st.session_state.user["role"]

    if role == "Admin":

        delete_id = st.text_input("Enter Student ID to Delete")
        delete_name = st.text_input("Or Enter Student Name")

        if st.button("Delete Student"):

            if delete_id:
                supabase.table("students").delete().eq("student_id", delete_id).execute()
                st.success("Student deleted successfully")

            elif delete_name:
                supabase.table("students").delete().eq("student_name", delete_name).execute()
                st.success("Student deleted successfully")

            else:
                st.warning("Enter Student ID or Name")
