import streamlit as st
import pandas as pd
from database import supabase

def show():
    st.title("Students Owing Fees")

    students = supabase.table("students").select("*").execute().data
    payments = supabase.table("payments").select("*").execute().data
    fees = supabase.table("school_fees").select("*").execute().data

    df_students = pd.DataFrame(students)
    df_payments = pd.DataFrame(payments)
    df_fees = pd.DataFrame(fees)

    st.write("Students list")
    st.dataframe(df_students)
