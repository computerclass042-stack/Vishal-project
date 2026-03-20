import streamlit as st
import math

st.set_page_config(page_title="Advanced Calculator", page_icon="🔢")

st.title("🔢 Advanced Calculator")

# Sidebar mein options
st.sidebar.header("Operations")
options = [
    "1. Plus (+)", "2. Minus (-)", "3. Multiply (*)", "4. Divide (/)",
    "5. Square (x²)", "6. Square Root (√)", "7. Cube (x³)", "8. Cube Root (∛)"
]
choice = st.sidebar.selectbox("Choose operation:", options)

# Logic for Two Number Operations
if any(op in choice for op in ["Plus", "Minus", "Multiply", "Divide"]):
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Enter first number:", value=0.0)
    with col2:
        b = st.number_input("Enter second number:", value=0.0)
    
    if st.button("Calculate"):
        if "Plus" in choice:
            st.success(f"Result = {a + b}")
        elif "Minus" in choice:
            st.success(f"Result = {a - b}")
        elif "Multiply" in choice:
            st.success(f"Result = {a * b}")
        elif "Divide" in choice:
            if b == 0:
                st.error("Error: Cannot divide by zero")
            else:
                st.success(f"Result = {a / b}")

# Logic for One Number Operations
else:
    a = st.number_input("Enter number:", value=0.0)
    
    if st.button("Calculate"):
        if "Square (x²)" in choice:
            st.success(f"Result = {a ** 2}")
        elif "Square Root (√)" in choice:
            st.success(f"Result = {math.sqrt(a) if a >= 0 else 'Invalid Input'}")
        elif "Cube (x³)" in choice:
            st.success(f"Result = {a ** 3}")
        elif "Cube Root (∛)" in choice:
            st.success(f"Result = {a ** (1/3)}")
