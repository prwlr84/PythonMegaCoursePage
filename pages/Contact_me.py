import streamlit as st
from send_email import send_email

st.header('Mail me')

with st.form(key='contact_form'):
    email = st.text_input('E-mail')
    text = st.text_area('Message')
    button = st.form_submit_button('Submit')
    msg = f'''\
Subject: New message from {email}
    
From: {email}
{text}
'''
    if button:
        send_email(msg)
        st.info('Message sent')
