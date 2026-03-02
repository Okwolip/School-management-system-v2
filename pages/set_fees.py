import streamlit as st
from database import supabase

def show():
    st.title("Set School Fees")

    session = st.text_input("Session")
    term = st.selectbox("Term", ["1st Term", "2nd Term", "3rd Term"])
    section = st.selectbox("Section", ["Nursery", "Primary", "Secondary"])
    amount = st.number_input("Amount", min_value=0)

    if st.button("Save Fee"):
        supabase.table("school_fees").insert({
            "session": session,
            "term": term,
            "section": section,
            "amount": amount
        }).execute()

        st.success("Fees saved")
