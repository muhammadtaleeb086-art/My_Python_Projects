import streamlit as st

st.title("Simple Calculator")

# Number inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.radio(
    "Choose operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Button to calculate
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by 0")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")

# python -m streamlit run calculator_app.py
