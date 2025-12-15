import streamlit as st

# Registration Form
with st.form(key="reg_form"):
    st.header("Registration Form")
    first_name = st.text_input(key="fname", label="First Name")
    last_name = st.text_input(key="lname", label="Last Name")
    age = st.slider("Age", 10, 100, 25, 1)
    addr = st.text_area("Address")
    submit_btn = st.form_submit_button("Submit", type="primary")

# form submit handling must be done outside form `with` block
if submit_btn:
    # validate form data
    err_message = ""
    is_error = False
    if not first_name:
        is_error = True
        err_message += "First name cannot be empty.\n"
    if not last_name:
        is_error = True
        err_message += "Last name cannot be empty.\n"
    if not addr:
        is_error = True
        err_message += "Address cannot be empty.\n"
    # if any error, display the error
    if is_error:
        st.error(err_message)
    # otherwise display success message
    else:
        message = f"Successfully registered: {st.session_state['fname']} {st.session_state['lname']}.\nAge: {age}. Living at {addr}"
        st.success(message)