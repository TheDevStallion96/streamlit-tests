import streamlit as st

# Title of the app
st.title('Interactive Streamlit App Example')

# Text input for user's name
name = st.text_input('What is your name?', '')

if st.button("Dashboard"):
    st.switch_page("streamlit_app.py")
if st.button("Settings"):
    st.switch_page("pages/settings.py")

# Selectbox for age range
age_range = st.selectbox(
    'What is your age range?',
    ('<18', '18-30', '31-45', '46-60', '>60')
)

# Color picker for favorite color
favorite_color = st.color_picker('Pick your favorite color', '#00f900')

with st.sidebar:
	st.title('ChatBot UI')
	st.header("ChatBot")
