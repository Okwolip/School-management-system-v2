import streamlit as st
from database import supabase

def login(username, password):
    response = supabase.table("users").select("*").eq("username", username).eq("password", password).execute()

    if response.data:
        return response.data[0]
    return None


def login_page():
    st.title("School Management System Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login(username, password)
        if user:
            st.session_state.user = user
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")
