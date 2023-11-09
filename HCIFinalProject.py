# fvusegukbkfawegbgkse
import streamlit as st
# import pandas as pd
# To run: streamlit run example3.py

st.header("Love Zodiac Compatibility")
st.title("Brought to you by Group 3")
# st.sidebar.title("Brought to you by Group 3")

#st.sidebar.text_input("YOUR NAME: ")
st.text_input("YOUR NAME: ")
conv_type = st.selectbox("Select your Zodiac Sign: ", options=["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"])

st.text_input("PARTNER'S NAME: ")
conv_type = st.selectbox("Select your Zodiac Sign: ", options= ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"])

#results = "Chances "
st.sidebar.text_area("Enter your comments here")
