import streamlit as st
from auth import login_page
from pages import register_student, view_students, process_payment
from pages import payment_records, set_fees, students_owing, manage_users

st.set_page_config(page_title="School Management System", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    login_page()
else:
    st.sidebar.title("Menu")

    menu = [
        "Register Student",
        "View Students",
        "Process Payment",
        "Payment Records",
        "Set School Fees",
        "Students Owing",
        "Manage Users",
        "Logout"
    ]

    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Register Student":
        register_student.show()

    elif choice == "View Students":
        view_students.show()

    elif choice == "Process Payment":
        process_payment.show()

    elif choice == "Payment Records":
        payment_records.show()

    elif choice == "Set School Fees":
        set_fees.show()

    elif choice == "Students Owing":
        students_owing.show()

    elif choice == "Manage Users":
        manage_users.show()

    elif choice == "Logout":
        st.session_state.user = None
        st.rerun()
