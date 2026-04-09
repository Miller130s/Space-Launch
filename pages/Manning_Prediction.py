from numpy import ceil
import streamlit as st
from PIL import Image
import pandas as pd
import joblib
import math



missions = st.slider("Select the number of missions", min_value=1, max_value=10)
tasks_per_mission = st.slider("Select the average number of important tasks per mission", min_value=1, max_value=500)
total_tasks = missions * tasks_per_mission
# st.dataframe(pd.read_csv("data/man.csv"))
power_df = pd.DataFrame({
    "missions": [missions],
    "tasks_per_mission": [tasks_per_mission],
    "total_tasks": [total_tasks]
    
})

data = joblib.load('manpower_predict.joblib')

model = data["model"]
manpower_prediction = model.predict(power_df)

st.write("Predicted Manpower:", math.ceil(manpower_prediction[0]))