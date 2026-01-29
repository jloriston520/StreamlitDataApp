import streamlit as st
import pandas as pd
import plotly.express as px
from apis import apod_generator
import os

st.title("Water Quality Dashboard")
st.header("Internship ready ")
st.subheader("Jeremiah Loriston")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview",
     "Data Display",
    "Insight",
     "NASA's APOD"]
)

with tab1:
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Google")

with tab2:
    fig1 = px.line(df,
                   x="Time",
                   y= "Temperature (c)")
    st.plotly_chart(fig1)

    fig2 = px.scatter(df,
                      x= "ODO mg/L",
                      y= "Temperature (c)",
                      color = "pH")
    st.plotly_chart(fig2)

with tab3:
    fig3 = px.scatter_3d(df,
                      x= "Longitude",
                      y="Latitude",
                      z= "Total Water Column (m)",
                         color= "Temperature (c)")
    fig3.update_scenes(zaxis_autorange= "reversed")
    st.plotly_chart(fig3)


with tab4:
    st.header("Astronomy picture of the day")
    st.divider()
    #TODO: call a function that generates the the
    url = "https://api.nasa.gov/planetary/apod?api_key="
    response = apod_generator(url, os.getenv("NASA_API_KEY"))

    #TODO: using the streamlit method, display the APOD image and title and other features
    st.title(response["title"])
    st.write(response["date"])
    st.write(response["explanation"])
    st.image(response["hdurl"])



