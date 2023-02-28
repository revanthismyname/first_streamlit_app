import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMG_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

st.title("Dashboard - Titanic Data")

img = image.imread(IMG_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

genders = st.selectbox("Select the Gender: ", df["sex"].unique())
col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df["sex"] == genders], x = "survived")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(data_frame = df, x = "sex", y = "survived")
col2.plotly_chart(fig_2, use_container_width=True)