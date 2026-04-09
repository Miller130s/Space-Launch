from importlib.metadata import metadata
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
from scipy import stats
import pydeck as pdk
from PIL import Image




# st.title("Manning Prediction Model")


import base64

def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

image = "Flacon rocket.png"
encoded = get_base64(image)

# --- Background image ---
st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{encoded}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)

# --- Layout + fixed title ---
st.markdown("""
<style>

/* Remove top padding */
.block-container {
    padding-top: 0rem;
}

/* FIXED TITLE (fully controllable now) */
.fixed-title {
    position: fixed;
    top: 50px;              /* 🔥 CHANGE THIS to move up/down */
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 42px;
    font-weight: 200;
    z-index: 9999;

    /* 👇 THIS makes adjustments actually apply */
    width: 100%;
    text-align: center;
    pointer-events: none;
}

/* Content spacing under title */
.main-content {
    margin-top: 100px;      /* 🔥 adjust to prevent overlap */
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="fixed-title">Space Launch</div>', unsafe_allow_html=True)
st.markdown('<div class="main-content">', unsafe_allow_html=True)



# st.video("https://youtu.be/Ewvs3fxxj9M?si=g1DG0YuEaKqQTfYu", autoplay=False)


# page_1 = st.Page("pages/page_1.py", title="Page 1")

# page_nav = st.navigation(["pages/page_1.py"])

# page_nav.run()