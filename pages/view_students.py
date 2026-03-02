import streamlit as st
import pandas as pd
from database import supabase

st.title("All Registered Students")

response = supabase.table("students").select("*").order("created_at", desc=True).execute()

if response.data:
    df = pd.DataFrame(response.data)

    columns = [
        "student_id",
        "student_name",
        "date_of_birth",
        "parent_name",
        "parent_phone",
        "section",
        "session"
    ]

    df = df[columns]

    st.dataframe(df, use_container_width=True)
else:
    st.info("No students registered yet.")
