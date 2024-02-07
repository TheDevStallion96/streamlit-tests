import streamlit as st

# Title of the app
st.title('Interactive Streamlit App Example')

# Text input for user's name
name = st.text_input('What is your name?', '')

# Selectbox for age range
age_range = st.selectbox(
    'What is your age range?',
    ('<18', '18-30', '31-45', '46-60', '>60')
)

# Color picker for favorite color
favorite_color = st.color_picker('Pick your favorite color', '#00f900')

# Button to submit choices
if st.button('Submit'):
    st.write(f'Hello, {name}!')
    st.write(f'Your age range is: {age_range}')
    st.write(f'Your favorite color is: ', favorite_color)
else:
    st.write('Please input your details and press submit.')

