import streamlit as st
from database import supabase

def show():
    st.title("Set School Fees")

    session = st.text_input("Session")
    term = st.selectbox("Term", ["1st Term", "2nd Term", "3rd Term"])
    amount = st.number_input("Amount")

    if st.button("Save Fee"):
        data = {
            "session": session,
            "term": term,
            "amount": amount
        }

        supabase.table("school_fees").insert(data).execute()
        st.success("Fees saved")
