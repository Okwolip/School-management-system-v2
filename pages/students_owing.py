import streamlit as st
import pandas as pd
from database import supabase

def show():
    st.title("Students Owing Fees")

    students = supabase.table("students").select("*").execute()
    payments = supabase.table("payments").select("*").execute()
    fees = supabase.table("school_fees").select("*").execute()

    if students.data and fees.data:
        df_students = pd.DataFrame(students.data)
        df_payments = pd.DataFrame(payments.data) if payments.data else pd.DataFrame()

        results = []

        for _, student in df_students.iterrows():
            section = student["section"]
            session = student["session"]

            fee = [f for f in fees.data if f["section"] == section and f["session"] == session]

            if fee:
                total_fee = fee[0]["amount"]
                paid = df_payments[df_payments["student_id"] == student["student_id"]]["amount_paid"].sum() if not df_payments.empty else 0
                balance = total_fee - paid

                if balance > 0:
                    results.append({
                        "student_id": student["student_id"],
                        "student_name": student["student_name"],
                        "balance": balance
                    })

        if results:
            st.dataframe(pd.DataFrame(results))
