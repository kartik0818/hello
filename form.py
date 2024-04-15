import streamlit as st
st.write("""
# My first app
Hello world!
""")
st.checkbox('yes')
st.checkbox('No')
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a bike',['GT650', 'MT15', 'S1000RR'])
st.select_slider('Pick a budget', ['2LAKHS', '10LAKHS', '20LAKHS'])
st.slider('Pick a MILEAGE ', 0,50)
file = st.file_uploader("Pick a picture")
