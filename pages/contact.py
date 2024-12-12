import streamlit as st


st.image('personal.svg', use_column_width=True)
def contact_form():
    st.title('Contact Form')

    name = st.text_input('Your Name')
    email = st.text_input('Your Email')
    message = st.text_area('Your Message', height=200)

    if st.button('Submit'):
        if name and email and message:
            # Here, you can add code to process the form data, such as sending an email
            st.success('Message sent successfully!')
        else:
            st.error('Please fill in all fields.')

contact_form()
st.image('contact.svg', use_column_width=True)
