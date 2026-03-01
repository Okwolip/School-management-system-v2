import streamlit as st
from database import supabase

def show():
    st.title("Process School Fee Payment")

    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")

    session = st.text_input("Session")
    term = st.selectbox("Term", ["1st Term", "2nd Term", "3rd Term"])
    amount = st.number_input("Amount Paid")

    if st.button("Record Payment"):

        data = {
            "student_id": student_id,
            "student_name": student_name,
            "session": session,
            "term": term,
            "amount_paid": amount
        }

        supabase.table("payments").insert(data).execute()

        st.success("Payment recorded successfully")
