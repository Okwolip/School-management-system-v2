import streamlit as st
import pandas as pd
from database import supabase

def show():
    st.title("Payment Records")

    response = supabase.table("payments").select("*").execute()

    if response.data:
        df = pd.DataFrame(response.data)
        st.dataframe(df)
