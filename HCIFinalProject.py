import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
 background-color: #fcfafc;
 color: #5d0403}}
 
 [data-testid="stSidebar"] > div:first-child {{
 background-color: #fce8ee;}}
 
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
#contact options
option = st.sidebar.selectbox("How do you prefer to be contacted?", options=[
    "", "Email", "Phone Call", "Text Message", "I prefer not to be contacted."])

agree_terms = st.sidebar.checkbox("💌 I agree to the terms and conditions for sharing my contact info.")

if option and agree_terms:
    if option == "Email":
        st.sidebar.write("Please enter your email below:")
        enter_email = st.sidebar.text_input("Email")
        if enter_email:
            st.sidebar.write(f"Thank you! You will receive a message at {enter_email}")
    elif option == "Phone Call":
        st.sidebar.write("Please enter your phone number below for a call:")
        phone_number = st.sidebar.text_input("Phone Number")
        if phone_number:
            st.sidebar.write(f"Thank you! We will contact you at {phone_number} for a phone call.")
    elif option == "Text Message":
        st.sidebar.write("Please enter your phone number below for a text:")
        phone_number = st.sidebar.text_input("Phone Number")
        if phone_number:
            st.sidebar.write(f"Thank you! We will send a text to {phone_number}.")

# User Input for User
user_name = st.text_input("YOUR NAME:")
user_zodiac = st.selectbox("Select your Zodiac Sign☽:", options=["Capricorn ♑️", "Aquarius ♒️", "Pisces ♓️", "Aries ♈️", "Taurus ♉️", "Gemini ♊️", "Cancer ♋️", "Leo ♌️", "Virgo ♍️", "Libra ♎️️", "Scorpio ♏️", "Sagittarius ♐️"])
user_gender = st.selectbox("Select your Gender:", options=["", "Female", "Male", "Non-Binary"])
user_age = st.slider('How old are you?', 0, 130, 25)
st.write("You're", user_age, 'years old')


# Zodiac sign data with date ranges
zodiac_data = {
    'Zodiac Sign': ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'],
    'Date Range': ['Mar 21 - Apr 19', 'Apr 20 - May 20', 'May 21 - Jun 20', 'Jun 21 - Jul 22', 'Jul 23 - Aug 22', 'Aug 23 - Sep 22', 'Sep 23 - Oct 22', 'Oct 23 - Nov 21', 'Nov 22 - Dec 21', 'Dec 22 - Jan 19', 'Jan 20 - Feb 18', 'Feb 19 - Mar 20']
}

# Create a DataFrame from the zodiac data
zodiac_df = pd.DataFrame(zodiac_data)

# Create Streamlit app
st.title('Zodiac Sign Date Ranges')

# Display the zodiac DataFrame in the sidebar without index numbers
st.sidebar.title('Zodiac Sign Date Ranges')
st.sidebar.write(zodiac_df.set_index('Zodiac Sign'), index=False)


# User Input for Partner
partner_name = st.text_input("PARTNER'S NAME:")
partner_zodiac = st.selectbox("Select your Partner's Zodiac Sign☽:", options=["Capricorn ♑️", "Aquarius ♒️", "Pisces ♓️", "Aries ♈️", "Taurus ♉️", "Gemini ♊️", "Cancer ♋️", "Leo ♌️", "Virgo ♍️", "Libra ♎️️", "Scorpio ♏️", "Sagittarius ♐️"])
partner_gender = st.selectbox("Select your Partner's Gender:", options=["","Female", "Male", "Non-Binary"])
partner_age = st.slider("How old is your partner?", 0, 130, 25)
st.write("Your partner is", partner_age, "years old")

def generate_popularity_data():
    zodiac_signs = [
        "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
        "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"
    ]
    popularity_data = np.random.randint(10, 100, size=(len(zodiac_signs), len(zodiac_signs)))
    return popularity_data, zodiac_signs

st.sidebar.title('✨Popular Zodiac Combinations✨')

popularity_matrix, signs = generate_popularity_data()

popularity_df = pd.DataFrame(popularity_matrix, columns=signs, index=signs)

most_popular_combination = popularity_df.stack().idxmax()
st.sidebar.write(f"♡Most popular combination this week♡: {most_popular_combination}")

fig, ax = plt.subplots(figsize=(6, 4))
popularity_df.plot(kind='line', ax=ax, marker='o')
ax.set_xlabel('Zodiac Signs')
ax.set_ylabel('Popularity Score')
ax.set_title('Zodiac Popularity')
ax.legend(loc='upper right')
st.sidebar.pyplot(fig)

def generate_compatibility_data():
    zodiac_signs = [
        "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
        "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"
    ]
    compatibility_data = np.random.rand(len(zodiac_signs), len(zodiac_signs)) * 50
    return compatibility_data, zodiac_signs

if st.button("Submit"):
    if user_name and user_zodiac and user_gender and partner_name and partner_zodiac and partner_gender:
        st.success("You’ve successfully submitted your info, let’s see your matches! 💟")
        compatibility_matrix, signs = generate_compatibility_data()

        # Filter compatibility scores for selected user and partner sign
        user_index = signs.index(user_zodiac)
        partner_index = signs.index(partner_zodiac)
        user_compat_scores = compatibility_matrix[user_index]
        partner_compat_scores = compatibility_matrix[:, partner_index]

        # Create DataFrame for the selected compatibility scores
        chart_data = pd.DataFrame({
            'Your Compatibility': user_compat_scores,
            "Partner's Compatibility": partner_compat_scores
        }, index=signs)

        # Plotting the bar chart using Matplotlib with different colors for bars
        fig, ax = plt.subplots(figsize=(10, 6))
        chart_data.plot(kind='bar', ax=ax, color=['skyblue', 'salmon'])
        ax.set_xlabel('Zodiac Signs')
        ax.set_ylabel('Compatibility Score (%)')
        ax.set_title('Zodiac Compatibility')
        ax.set_xticklabels(chart_data.index, rotation=45)
        ax.legend()
        st.pyplot(fig)
      
        st.subheader('✨Matches and Potential Couples Map✨')
        df = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [25.7617, -80.1918],
            columns=['lat', 'lon'])

        st.map(df)
    else:
        st.error("Please fill out all the fields. 🚨")
