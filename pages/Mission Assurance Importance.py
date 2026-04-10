from importlib.metadata import metadata
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
from scipy import stats
import pydeck as pdk
from PIL import Image

st.title("Why Mission Assurance is Important")
st.image("Successfrfr.png")
st.write("The graph above shows the total success percentage of launches from 2010 to 2023. The data indicates that while there have been fluctuations in success rates, there is a general trend towards improvement over time. This underscores the importance of mission assurance in ensuring the reliability and success of space missions, as even a small percentage of failures can have significant consequences in terms of cost, safety, and scientific outcomes. The learning phase Identified in the graph above is the time it took SpaceX to learn how to land a booster and reliably get to space.")


