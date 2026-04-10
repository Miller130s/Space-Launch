from importlib.metadata import metadata
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
from scipy import stats
import pydeck as pdk
from PIL import Image

st.title("Future Trends in Launch Volume and Payload Weight")

st.image("Vandenberg_Prediction.png")
st.write("The graph above shows the predicted number of launches from Vandenberg Space Force Base from 2026 to 2030. The prediction is based on historical data and trends in the space industry. The graph indicates a steady increase in the number of launches, suggesting a growing demand for space access and exploration in the coming years.")

st.image("Cape_Prediction.png")
st.write("The graph above shows the predicted number of launches from Cape Canaveral Space Force Station from 2026 to 2030. The prediction is based on the recent growth in launches from this site.")

st.image("SpaceX_Payload_Weight_Road_o_2030.png")
st.write("According to trend analysis we predict a growth in the number of heavy payload launches as well as a increase in payload weight.")

