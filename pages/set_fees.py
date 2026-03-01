import streamlit as st
from database import supabase
import pandas as pd

def show():
    st.title("Set School Fees")

    st.subheader("Configure School Fees")

    session = st.selectbox("Session", ["2025/2026", "2026/2027", "2027/2028"])

    term = st.selectbox("Term", [
        "1st Term",
        "2nd Term",
        "3rd Term"
    ])

    section = st.selectbox("Section", [
        "Nursery",
        "Primary",
        "Secondary"
    ])

    amount = st.number_input("Fee Amount", min_value=0)

    if st.button("Save Fees"):

        data = {
            "session": session,
            "term": term,
            "section": section,
            "amount": amount
        }

        supabase.table("school_fees").insert(data).execute()

        st.success("Fees saved successfully")

    st.divider()

    st.subheader("Existing Fee Structure")

    response = supabase.table("school_fees").select("*").execute()

    if response.data:
        df = pd.DataFrame(response.data)
        st.dataframe(df)
