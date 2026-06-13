# Energy Consumption Prediction using Machine Learning

## Project Overview

This project predicts household energy consumption using Machine Learning. The model is trained on the Household Electric Power Consumption dataset and estimates Global Active Power based on electrical measurements and time-related features.

## Features Used

* Hour
* Day
* Month
* Weekday
* Voltage
* Global Intensity
* Sub Metering 1
* Sub Metering 2
* Sub Metering 3

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

## Machine Learning Model

* Random Forest Regressor

## Model Performance

* Train R² Score: 0.9998
* Test R² Score: 0.9987
* MAE: 0.0214

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Deployment using Streamlit

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Future Improvements

* XGBoost implementation
* Time-series forecasting features
* Advanced feature engineering
* Cloud deployment

## Author

Kiran Kumar
