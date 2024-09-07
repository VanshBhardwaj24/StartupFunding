import streamlit as st
import pandas as pd
import time

st.title('Startup dashboard')
st.header("I am learning Streamlit")
st.subheader("This is a subheader")
st.write("This is a normal text")

st.markdown("""
            ### This is a markdown
            - Fruits
            - Vegetables
            - Meat
    """)

st.code("""
    def foo(x):
        return x**2
    x = foo(3)
        
"""
)

st.latex('x^2 +y^2 = z^2')

import pandas as pd

df = pd.DataFrame({
    'name': ['John', 'Jane', 'Doe'],
    'age': [23, 24, 25],
    'marks': [90,89,20]
})

st.write(df)

st.metric('This is revenue', '$1000','3%')

st.json({
    'name': ['John', 'Jane', 'Doe'],
    'age': [23, 24, 25],
    'marks': [90,89,20]})

st.image('img.jpeg')

st.sidebar.write('This is a sidebar')

col1, col2 = st.columns(2)

with col1:
    st.image('img.jpeg')

with col2:
    st.image('img.jpeg')

st.error('Login failed')
st.success('Login successful')
st.warning('This is a warning')
st.info('This is an info') 

progressbar = st.progress(0)
for i in range(100):
    progressbar.progress(i+1)
    # time.sleep(0.1)

st.text_input('Enter your name')
st.number_input('Enter your age')
st.date_input('Enter your birthdate')

import streamlit as st

email = st.text_input('Enter your email')
password = st.text_input('Enter your password', type='password')
genre = st.selectbox('Select your favourite genre', ['Comedy', 'Drama', 'Thriller'])

btn = st.button('Login')
st.checkbox('I agree to the terms and conditions')

if btn:
    if email == 'nitish@gmail.com' and password == '1234':
        st.success('Login successful')
        st.balloons()
        st.write(f'Your favourite genre is {genre}')
    else:
        st.error('Login failed')

import streamlit as st
import pandas as pd

file = st.file_uploader('Upload a file type: csv')

if file is not None:
    df = pd.read_csv(file)
    st.write(df.describe())
