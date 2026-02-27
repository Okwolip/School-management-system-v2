import streamlit as st
from database import supabase

def show():
    st.title("Manage Users")

    username = st.text_input("Username")
    password = st.text_input("Password")
    role = st.selectbox("Role", ["Admin", "Teacher", "Cashier"])

    if st.button("Create User"):
        data = {
            "username": username,
            "password": password,
            "role": role
        }

        supabase.table("users").insert(data).execute()
        st.success("User created")
