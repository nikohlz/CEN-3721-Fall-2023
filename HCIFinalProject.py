import streamlit as st
# import pandas as pd
# To run: streamlit run example3.py

st.header("Love Zodiac Compatibility")
st.title("Brought to you by Group 3")
# st.sidebar.title("Brought to you by Group 3")

# Text Input 
st.text_input("YOUR NAME: ")
# Selectbox 
conv_type = st.selectbox("Select your Zodiac Sign: ", options=["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"])
conv_type = st.selectbox("Select your Gender: ", options=["Female", "Male", "Non-Binary"])

st.text_input("PARTNER'S NAME: ")
conv_type = st.selectbox("Select your Zodiac Sign: ", options= ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"])
conv_type = st.selectbox("Select your Gender: ", options=["Female", "Male", "Non-Binary"])

#results = "Chances "
st.sidebar.text_area("Enter your comments here")
