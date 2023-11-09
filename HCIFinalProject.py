import streamlit as st

st.header("Love Zodiac Compatibility")
st.title("Brought to you by Group 3")

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
