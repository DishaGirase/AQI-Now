# STREAMLIT APP: AIR QUALITY INDEX (AQI) DASHBOARD

import streamlit as st
import numpy as np
import pandas as pd
import requests
import plotly.graph_objects as go
import joblib
import os

# CONFIGURATION

st.set_page_config(
    page_title="AI-Powered AQI Dashboard",
    layout="wide",
)

# CONSTANTS

API_KEY = "74bd8aa4ee544b2d53c36cf5ef9a93ea"  
MODEL_PATH = os.path.join("Aqi_model", "aqi_model.joblib")

# STYLES

st.markdown(
    """
    <style>
        /* Main app container */
        .css-18e3th9 {
            background-color: white;
            color: black;
        }

        /* Sidebar background */
        .css-1d391kg {
            background-color: #f0f2f6;
        }

        /* AQI category styles */
        .big-font { font-size: 24px !important; font-weight: bold; }
        .good {color: #00b050;}
        .moderate {color: #92d050;}
        .usg {color: #ffc000;}
        .unhealthy {color: #ff0000;}
        .very-unhealthy {color: #7030a0;}
        .hazardous {color: #7f0000;}

        /* Footer */
        .footer { font-size: 13px; text-align: center; color: gray; margin-top: 50px; }

        /* Buttons */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# HELPER FUNCTIONS

def get_aqi_category(aqi_value):
    if aqi_value <= 50:
        return "Good", "good", "Air quality is considered satisfactory."
    elif aqi_value <= 100:
        return "Moderate", "moderate", "Air quality is acceptable."
    elif aqi_value <= 150:
        return "Unhealthy for Sensitive Groups", "usg", "May affect sensitive groups."
    elif aqi_value <= 200:
        return "Unhealthy", "unhealthy", "Everyone may experience negative effects."
    elif aqi_value <= 300:
        return "Very Unhealthy", "very-unhealthy", "Health alert: everyone may feel effects."
    else:
        return "Hazardous", "hazardous", "Emergency conditions—avoid outdoor activities."

def fetch_coordinates(city, country=None, api_key=None):
    try:
        query = f"{city},{country}" if country else city
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=1&appid={api_key}"
        res = requests.get(url, timeout=10)
        data = res.json()
        if len(data) == 0:
            return None, None
        return data[0]['lat'], data[0]['lon']
    except Exception:
        return None, None

def fetch_aqi_from_api(lat, lon, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        res = requests.get(url, timeout=10)
        data = res.json()
        if "list" not in data or len(data["list"]) == 0:
            return None, None
        aqi = data["list"][0]["main"]["aqi"]
        components = data["list"][0]["components"]
        epa_scale = [50, 100, 150, 200, 300] 
        api_aqi = epa_scale[aqi - 1]
        return api_aqi, components
    except Exception:
        return None, None

def predict_aqi_with_model(features):
    
    model_path = os.path.join("Aqi_model", "aqi_model.joblib")
    
    if not os.path.exists(model_path):
        st.warning(f"ML model '{model_path}' not found. Skipping model prediction.")
        return None
    try:
        model = joblib.load(model_path)
        prediction = model.predict([features])[0]
        return round(float(prediction))
    except Exception as e:
        st.error(f"Error predicting AQI: {e}")
        return None

def create_gauge_chart(aqi_value):
    category, color_class, _ = get_aqi_category(aqi_value)
    color_map = {
        "good": "#00b050",
        "moderate": "#92d050",
        "usg": "#ffc000",
        "unhealthy": "#ff0000",
        "very-unhealthy": "#7030a0",
        "hazardous": "#7f0000",
    }
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=aqi_value,
        title={'text': "AQI"},
        gauge={'axis': {'range': [0, 500]},
               'bar': {'color': color_map[color_class]},
               'steps': [
                   {'range': [0,50], 'color': '#00b050'},
                   {'range': [51,100], 'color': '#92d050'},
                   {'range': [101,150], 'color': '#ffc000'},
                   {'range': [151,200], 'color': '#ff0000'},
                   {'range': [201,300], 'color': '#7030a0'},
                   {'range': [301,500], 'color': '#7f0000'}]}))
    fig.update_layout(height=350, margin=dict(t=50, b=0))
    return fig
    

# LOCATION INPUT

st.header("AQI Prediction Dashboard")

test_cities = [
    "Ahmedabad", "Delhi", "Mumbai", "Bengaluru", "Chennai",
    "Kolkata", "Hyderabad", "Pune", "Jaipur", "Lucknow"
]

st.markdown("**Select a city from the list or enter a city manually:**")
city_dropdown = st.selectbox("Quick Select City", ["--Select--"] + test_cities)
city_manual = st.text_input("Or type your city name here", "")


if city_manual.strip():
    city = city_manual.strip()
elif city_dropdown != "--Select--":
    city = city_dropdown
else:
    st.warning("Please select a city or enter a city name to begin.")
    st.stop()

# FETCH DATA

lat, lon = fetch_coordinates(city=city, api_key=API_KEY)
if lat is None:
    st.error("Unable to fetch coordinates. Check city name or API Key.")
    st.stop()

api_aqi, pollutants = fetch_aqi_from_api(lat, lon, API_KEY)

st.subheader(f"📍 Location: {city.title()}")
st.write(f"Coordinates: {lat:.2f}, {lon:.2f}")

# MODEL PREDICTION

predicted_aqi = None
if pollutants:
    st.write("### Real-Time Pollutants (μg/m³)")
    st.dataframe(pd.DataFrame([pollutants]).T.rename(columns={0:"Concentration"}))

   
    model_features = [
        pollutants.get("pm2_5",0),
        pollutants.get("pm10",0),
        pollutants.get("no", 0),
        pollutants.get("no2",0),
        pollutants.get("nh3", 0),
        pollutants.get("co",0),
        pollutants.get("so2",0),
        pollutants.get("o3",0)
    ]

    predicted_aqi = predict_aqi_with_model(model_features)

# DISPLAY RESULTS

if predicted_aqi or api_aqi:
    col1, col2 = st.columns(2)

    with col1:
        if predicted_aqi:
            cat, color, desc = get_aqi_category(predicted_aqi)
            st.markdown(f'<p class="big-font {color}">Predicted AQI: {predicted_aqi} ({cat})</p>', unsafe_allow_html=True)
            st.write(f"Description: {desc}")
            st.plotly_chart(create_gauge_chart(predicted_aqi), use_container_width=True)

    with col2:
        if api_aqi:
            cat_api, color_api, desc_api = get_aqi_category(api_aqi)
            st.markdown(f'<p class="big-font {color_api}">API AQI: {api_aqi} ({cat_api})</p>', unsafe_allow_html=True)
            st.write(f"Description: {desc_api}")

    if predicted_aqi and api_aqi:
        match_accuracy = 100 - abs(predicted_aqi-api_aqi)/api_aqi*100
        st.success(f"Prediction Agreement: {match_accuracy:.2f}%")
else:
    st.error("No AQI data available to display.")

# HISTORICAL SESSION TRACKING


if "history" not in st.session_state:
    st.session_state["history"] = pd.DataFrame(columns=["City","Predicted AQI","API AQI"])

if predicted_aqi or api_aqi:
    new_row = {"City": city.title(), "Predicted AQI": predicted_aqi, "API AQI": api_aqi}
    st.session_state["history"] = pd.concat([st.session_state["history"], pd.DataFrame([new_row])], ignore_index=True)

if len(st.session_state["history"]) > 0:
    st.write("### Historical Predictions (this session)")
    st.dataframe(st.session_state["history"])

# FOOTER

st.markdown(
    """
    <div class="footer">
        Built with ❤️ using Streamlit, OpenWeatherMap API, and a custom ML model.<br>
        © 2026 AQI Dashboard Demo
    </div>
    """,
    unsafe_allow_html=True,
)
