import streamlit as st
# import pandas as pd
# To run:  streamlit run HCIFinalProject.py

st.set_page_config(page_title="Love Zodiac Compatibility",
                   layout= "wide" )

# Header and title
st.markdown(
    """
    <style>
    h1 {
        color: #ffa7d2;
    }

    body {
        color: #5d0403;
    }
    </style>

    <h1>Love Zodiac Compatibility</h1>
    <p>Brought to you by Group 3</p>
    """,
    unsafe_allow_html=True,
)

page_color = f"""
<style>
 [data-testid="stAppViewContainer"] > .main {{
 background-color: #fce8ee;
 color: #5d0403}}
 
 [data-testid="stSidebar"] > div:first-child {{
 background-color: #fcfafc;}}
 
 [data-testid="stHeader"] {{
 background: rgba(0,0,0,0);
 }}
 h1, h2, h3, h4, h5, h6, p {{
        color: #5d0403;
 }}
 </style>
"""
st.markdown(page_color, unsafe_allow_html=True)


st.sidebar.title("Any thoughts?")
st.sidebar.header("We want to hear from you!")
st.sidebar.selectbox("How do you prefer to be contacted?",options= [
    "", "Email", "Phone Call", "Text Message", "I prefer not to be contacted."])
#if st.sidebar.selectbox("Email"):
#    enter_email = st.text_input("Please enter your email we can contact you at!")


# User Input for User
user_name = st.text_input("YOUR NAME:")
user_zodiac = st.selectbox("Select your Zodiac Sign:", options=["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"])
user_gender = st.selectbox("Select your Gender:", options=["Female", "Male", "Non-Binary"])
user_age = st.slider('How old are you?', 0, 130, 25)
st.write("You're", user_age, 'years old')

# User Input for Partner
partner_name = st.text_input("PARTNER'S NAME:")
partner_zodiac = st.selectbox("Select your Partner's Zodiac Sign:", options=["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"])
partner_gender = st.selectbox("Select your Partner's Gender:", options=["Female", "Male", "Non-Binary"])
partner_age = st.slider("How old is your partner?", 0, 130, 25)
st.write("Your partner is", partner_age, "years old")

if st.button("Submit"):
    if user_name and user_zodiac and user_gender and partner_name and partner_zodiac and partner_gender:
        st.success("You’ve successfully submitted your info, let’s see your matches! 💟")
    else:
        st.error("Please fill out all the fields. 🚨")
