import streamlit as st
from PIL import Image
import pandas as pd
import joblib



Off_TDs = st.slider("Select the number of offensive touchdowns scored", min_value=1, max_value=100)
Off_Rank = st.slider("Select the Off rank of the team", min_value=1, max_value=133)
Def_Rank = st.slider("Select the Deff rank of the team", min_value=1, max_value=133)
Touchdowns = st.slider("Select how many TDs the team scored in total", min_value=1, max_value=300)
Yards_Play_Allowed = st.slider("Select the yards a team gave up per game on defense", min_value=1, max_value=700)
st.dataframe(df)
cfb_df = pd.DataFrame({
    "Off TDs": [Off_TDs],
    "Off Rank": [Off_Rank],
    "Def Rank": [Def_Rank],
    "Touchdowns": [Touchdowns],
    "Yards/Play Allowed": [Yards_Play_Allowed],
    
})
chosen = st.selectbox('Choose your model', ['Linear Regression'])


if chosen == 'Linear Regression':
    data = joblib.load('TEAMRANK.joblib')

model = data["model"]
Win_PCT_prediction = model.predict(cfb_df)

st.write("Predicted WIN%:", Win_PCT_prediction)