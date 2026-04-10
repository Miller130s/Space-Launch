from numpy import ceil
import streamlit as st
from PIL import Image
import pandas as pd
import joblib
import math



missions = st.slider("Select the number of missions happening at one time", min_value=1, max_value=10)
tasks_per_mission = st.slider("Select the average number of observers per mission (Average 30 A-C Observes)", min_value=1, max_value=500, value=30)
total_tasks = missions * tasks_per_mission
# shift = st.slider("Select the shift", min_value=1, max_value=3)
# locations = st.slider("Select the number of locations", min_value=1, max_value=3)
campaign_in_weeks = st.slider("Select the campaign duration in weeks", min_value=1, max_value=52, value=4)

# st.dataframe(pd.read_csv("data/man.csv"))
power_df = pd.DataFrame({
    "missions": [missions],
    "tasks_per_mission": [tasks_per_mission],
    "total_tasks": [total_tasks],
    # "shift": [shift],
    # "location": [locations],
    "campaign_in_weeks": [campaign_in_weeks]
})

data = joblib.load('PB_predict.joblib')

model = data["model"]
manpower_prediction = model.predict(power_df)
total = math.ceil(manpower_prediction[0])

weights = [0.2, 0.4, 0.4]
values = [math.floor(total * w) for w in weights]

# Fix rounding on last value
values[-1] = total - sum(values[:-1])

# st.write("ASO:", values[0])
# st.write("SLC4:", values[1])
# st.write("B398:", values[2])
st.write("Total MATS Needed:", total)
# ASO = st.write("Predicted MATS at ASO:", math.ceil(manpower_prediction[0] * 0.2))
# SLC4 = st.write("Predicted MATS at SLC4:", math.ceil(manpower_prediction[0] * 0.4))
# B398 = st.write("Predicted MATS at B398:", math.ceil(manpower_prediction[0] * 0.4))
# total = st.write(math.ceil(manpower_prediction[0]), "MATS needed in total for the campaign")