import streamlit as st
import pandas as pd
import numpy as np


st.title('Welcome to my :blue[First] Streamlit App :sunglasses:')

st.subheader("Data Science Internship :red[Assignment 1]")

btn_click_iris = st.button("Take me to Iris")
btn_click_titanic = st.button("Take me to Titanic")

if btn_click_iris:
    st.subheader("Welcome to the :red[Iris] Dataset")

elif btn_click_titanic:
    st.subheader("Welcome to the :red[Titanic] Dataset")

else:
    pass
