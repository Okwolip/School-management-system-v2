import streamlit as st
from database import supabase
import pandas as pd

def show():
    st.title("Process School Fee Payment")

    student_id = st.text_input("Student ID")

    if st.button("Fetch Student"):

        student = supabase.table("students").select("*") \
            .eq("student_id", student_id).execute()

        if student.data:

            student_data = student.data[0]

            st.success("Student Found")

            st.write("Name:", student_data["student_name"])
            st.write("Section:", student_data["section"])
            st.write("Session:", student_data["session"])

            term = st.selectbox("Term", [
                "1st Term",
                "2nd Term",
                "3rd Term"
            ])

            fee = supabase.table("school_fees").select("*") \
                .eq("section", student_data["section"]) \
                .eq("session", student_data["session"]) \
                .eq("term", term).execute()

            if fee.data:
                amount_to_pay = fee.data[0]["amount"]
                st.info(f"Fee for this term: {amount_to_pay}")

                amount_paid = st.number_input("Amount Paid", min_value=0)

                if st.button("Confirm Payment"):

                    payment_data = {
                        "student_id": student_data["student_id"],
                        "student_name": student_data["student_name"],
                        "session": student_data["session"],
                        "term": term,
                        "amount_paid": amount_paid
                    }

                    supabase.table("payments").insert(payment_data).execute()

                    st.success("Payment recorded successfully")

            else:
                st.warning("Fee not set for this section yet")

        else:
            st.error("Student not found")
