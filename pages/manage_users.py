import streamlit as st
from database import supabase

def show():
    st.title("Manage Users")

    role = st.session_state.user["role"]

    if role != "Admin":
        st.warning("Only admin can manage users")
        return

    username = st.text_input("Username")
    password = st.text_input("Password")
    role_select = st.selectbox("Role", ["Admin", "Teacher", "Cashier"])

    if st.button("Create User"):
        supabase.table("users").insert({
            "username": username,
            "password": password,
            "role": role_select
        }).execute()

        st.success("User created")
