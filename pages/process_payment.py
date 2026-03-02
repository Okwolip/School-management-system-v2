import streamlit as st
from database import supabase

def show():
    st.title("Process Payment")

    student_id = st.text_input("Student ID")

    if st.button("Fetch Student"):

        student = supabase.table("students") \
            .select("*") \
            .eq("student_id", student_id) \
            .execute()

        if student.data:

            student_data = student.data[0]

            st.write("Name:", student_data["student_name"])
            st.write("Section:", student_data["section"])

            term = st.selectbox("Term", ["1st Term", "2nd Term", "3rd Term"])

            fee = supabase.table("school_fees") \
                .select("*") \
                .eq("section", student_data["section"]) \
                .eq("session", student_data["session"]) \
                .eq("term", term) \
                .execute()

            if fee.data:
                amount = fee.data[0]["amount"]
                st.info(f"Fee: {amount}")

                paid = st.number_input("Amount Paid", min_value=0)

                if st.button("Confirm Payment"):
                    supabase.table("payments").insert({
                        "student_id": student_data["student_id"],
                        "student_name": student_data["student_name"],
                        "term": term,
                        "session": student_data["session"],
                        "amount_paid": paid
                    }).execute()

                    st.success("Payment recorded")
