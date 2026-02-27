import streamlit as st
from auth import login_page

st.set_page_config(page_title="School Management System", layout="wide")

if "user" not in st.session_state:
    login_page()
    st.stop()

st.sidebar.title("School Menu")

role = st.session_state.user["role"]

menu = [
    "Register Student",
    "View Students",
    "Process Payment",
    "Payment Records",
    "Students Owing"
]

if role == "Admin":
    menu.append("Set School Fees")
    menu.append("Manage Users")

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register Student":
    from pages import register_student
    register_student.show()

elif choice == "View Students":
    from pages import view_students
    view_students.show()

elif choice == "Process Payment":
    from pages import process_payment
    process_payment.show()

elif choice == "Payment Records":
    from pages import payment_records
    payment_records.show()

elif choice == "Set School Fees":
    from pages import set_fees
    set_fees.show()

elif choice == "Students Owing":
    from pages import students_owing
    students_owing.show()

elif choice == "Manage Users":
    from pages import manage_users
    manage_users.show()
