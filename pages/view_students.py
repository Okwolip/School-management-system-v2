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
