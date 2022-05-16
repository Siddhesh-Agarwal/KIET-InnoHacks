import time
from datetime import date
from random import random

import requests
import streamlit as st
from plotly.graph_objs import *
from core import random_book

st.set_page_config(
    page_title="Lucid | Dashboard",
    page_icon="../assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("../../README.md").read(),
    },
)
st.title("Dashboard")


@st.experimental_memo(show_spinner=False)
def get_quote():
    """
    Get a random quote (per day) from the API

    Returns
    -------
    quote: str
        A random quote.
    """
    ref_date = date(2022, 5, 15)
    cur_date = date.today()
    num = (cur_date - ref_date).days
    url = f"https://motivational-quote-api.herokuapp.com/quotes/id/{num + 1}"
    data = requests.get(url).json()
    quote = data["quote"]["quote"]
    person = data["quote"]["person"]
    return quote, person


# Motivational Quote
st.header("Motivational Quote")
quote, person = get_quote()
st.info(f'"{quote}" - {person}')

# Random Book Recommendation
# st.header("Book Recommendation")
# genre = st.selectbox(
#    label="Select a genre", options=open("core/GENRE").read().split("\n")
# )
# with st.expander("Show random book"):
#    img, name = random_book(genre)
#    col_1, col_2 = st.beta_columns(2)
#    with col_1:
#        st.image(image=img)
#    with col_2:
#        st.subheader(name)

col1, col2 = st.columns(2)

# Column 1
with col1:
    st.header("Blood pressure tracker")
    with st.expander("Show/Hide"):
        st.write("sample text")

    st.header("Calories burnt tracker")
    with st.expander("Show/Hide"):
        st.write("sample text")

    st.header("Sleep tracker")
    with st.expander("Show/Hide"):
        st.write("sample text")

# Column 2
with col2:
    st.header("BMI Calculator")
    with st.expander("Click here to Show/Hide"):
        w = st.number_input("weight (kg)", value=50, step=1)
        h = st.number_input("height (cm)", value=100, step=1)
        if st.button("Calculate BMI"):
            BMI = w / (h / 100) ** 2

            with st.spinner("Calculating..."):
                time.sleep(2.0 + random())

            st.info(f"Your BMI is {BMI:.2f}")
            if BMI > 30:
                st.error(f"You are obese.")
            elif BMI > 25:
                st.warning(f"You are overweight.")
            elif BMI > 18:
                st.success(f"You are normal.")
            else:
                st.warning(f"Your are underweight.")

    st.header("Sugar level tracker")
    with st.expander("Show/Hide"):
        st.write("sample text")

    st.header("Step trackers")
    with st.expander("Show/Hide"):
        st.write("sample text")

# Sidebar for navigation
with st.sidebar:
    st.title("Navigation")
    st.markdown(
        """
    <ul style="list-style-type:none">
        <li>✨ <a href="#motivational-quote"><b>Motivational Quote</b></a></li>
        <li>🧮 <a href="#bmi-calculator"><b>BMI Calculator</b></a></li>
        <li>📈 <a href="#blood-pressure-tracker"><b>Blood Pressure Tracker</b></a></li>
        <li>🩸 <a href="#sugar-level-tracker"><b>Sugar Level Tracker</b></a></li>
        <li>🔥 <a href="#calories-burnt-tracker"><b>Calories Burnt Tracker</b></a></li>
        <li>👟 <a href="#step-tracker"><b>Step Tracker</b></a></li>
        <li>😴 <a href="#sleep-tracker"><b>Sleep Tracker</b></a></li>
        <li>🔎 <a href="http://localhost:8080/"><b>Community Finder</b></a></li>
    </ul>
    """,
        unsafe_allow_html=True,
    )
