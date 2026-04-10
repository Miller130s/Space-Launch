from importlib.metadata import metadata
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
from scipy import stats
import pydeck as pdk
from PIL import Image

st.set_page_config(page_title="Global Space Launch", page_icon=":rocket:", layout="wide")

st.title("Global Space Launch")

st.image("shift.png")