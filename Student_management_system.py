# students = []

# def add_student(name, roll, course):
#     student = {"name": name, "roll": roll, "course": course}
#     students.append(student)
#     print(" Student added successfully!")

# def view_students():
#     if not students:
#         print("No students found.")
#     else:
#         for s in students:
#             print(f"Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")

# def search_student(roll):
#     for s in students:
#         if s['roll'] == roll:
#             print(f" Found: Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")
#             return
#     print(" Student not found.")

# def delete_student(roll):
#     for s in students:
#         if s['roll'] == roll:
#             students.remove(s)
#             print("🗑 Student deleted successfully!")
#             return
#     print(" Student not found.")

# while True:
#     print("\n--- Student Management System ---")
#     print("1. Add Student")
#     print("2. View Students")
#     print("3. Search Student")
#     print("4. Delete Student")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         name = input("Enter name: ")
#         roll = int(input("Enter roll number: "))
#         course = input("Enter course: ")
#         add_student(name, roll, course)

#     elif choice == "2":
#         view_students()

#     elif choice == "3":
#         roll = int(input("Enter roll number to search: "))
#         search_student(roll)

#     elif choice == "4":
#         roll = int(input("Enter roll number to delete: "))
#         delete_student(roll)

#     elif choice == "5":
#         print("Exiting program... Goodbye!")
#         break

#     else:
#         print("Invalid choice, try again.")

# python -m streamlit run Student_management_system.py

import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

st.title(" Student Management System")
st.write("Manage student records easily.")

# -----------------------------
# Session State
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Functions
# -----------------------------
def add_student(name, roll, course):

    # Check duplicate roll number
    for student in st.session_state.students:
        if student["Roll"] == roll:
            st.error("Roll Number already exists.")
            return

    st.session_state.students.append({
        "Name": name,
        "Roll": roll,
        "Course": course
    })

    st.success("Student Added Successfully")


def delete_student(roll):

    for student in st.session_state.students:
        if student["Roll"] == roll:
            st.session_state.students.remove(student)
            st.success("Student Deleted Successfully")
            return

    st.error("Student Not Found")


def search_student(roll):

    for student in st.session_state.students:
        if student["Roll"] == roll:
            st.success("Student Found")
            st.table(pd.DataFrame([student]))
            return

    st.error("Student Not Found")


# -----------------------------
# Sidebar Menu
# -----------------------------
menu = st.sidebar.radio(
    "Choose Option",
    [
        "Add Student",
        "View Students",
        "Search Student",
        "Delete Student"
    ]
)

# -----------------------------
# Add Student
# -----------------------------
if menu == "Add Student":

    st.header(" Add Student")

    name = st.text_input("Student Name")

    roll = st.number_input(
        "Roll Number",
        min_value=1,
        step=1
    )

    course = st.text_input("Course")

    if st.button("Add Student"):

        if name and course:
            add_student(name, roll, course)
        else:
            st.warning("Please fill all fields.")


# -----------------------------
# View Students
# -----------------------------
elif menu == "View Students":

    st.header(" Student Records")

    if st.session_state.students:

        df = pd.DataFrame(st.session_state.students)

        st.dataframe(
            df,
            use_container_width=True
        )

        st.metric(
            "Total Students",
            len(df)
        )

    else:
        st.info("No Student Records Found.")


# -----------------------------
# Search Student
# -----------------------------
elif menu == "Search Student":

    st.header("🔍 Search Student")

    roll = st.number_input(
        "Enter Roll Number",
        min_value=1,
        step=1
    )

    if st.button("Search"):
        search_student(roll)


# -----------------------------
# Delete Student
# -----------------------------
elif menu == "Delete Student":

    st.header("🗑 Delete Student")

    roll = st.number_input(
        "Enter Roll Number",
        min_value=1,
        step=1
    )

    if st.button("Delete"):
        delete_student(roll)