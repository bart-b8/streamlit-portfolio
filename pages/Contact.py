import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms"): 
    user_email = st.text_input("Your email address:" )
    message = st.text_area("Your message:")
    button = st.form_submit_button('Submit')
    if button:
        send_email(user_email, message)
