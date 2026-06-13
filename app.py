import streamlit as st
import joblib
import pandas as pd

model=joblib.load("energy_consumption_model.pkl")

st.title("Energy Consumption Prediction")

hour=st.number_input("Hour",0,23)
day=st.number_input("Day",1,31)
month=st.number_input("Month",1,12)
weekday=st.number_input("Weekday",0,6)

voltage=st.number_input("Voltage")
global_intensity=st.number_input("Global Intensity")

sub1 = st.number_input("Sub Metering 1")
sub2 = st.number_input("Sub Metering 2")
sub3 = st.number_input("Sub Metering 3")

if st.button("Predict"):

    data = pd.DataFrame([[
        hour,
        day,
        month,
        weekday,
        voltage,
        global_intensity,
        sub1,
        sub2,
        sub3
    ]], columns=[
        'hour',
        'day',
        'month',
        'weekday',
        'Voltage',
        'Global_intensity',
        'Sub_metering_1',
        'Sub_metering_2',
        'Sub_metering_3'
    ])

    prediction = model.predict(data)

    st.success(
        f"Predicted Energy Consumption: {prediction[0]:.3f} KW"
    )