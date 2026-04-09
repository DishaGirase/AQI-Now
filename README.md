# AQI-Now: AI-Powered Air Quality Dashboard
#### Live Demo:
Check out the fully interactive dashboard here: [AQI-Now Dashboard](https://aqi-now-disha.streamlit.app)

This project predicts the Air Quality Index (AQI) using a combination of real-time API data and a custom Machine Learning model.
## Project Overview
**AQI-Now** is a **real-time**, **AI-powered Air Quality Index dashboard**. It predicts AQI using a **Random Forest ML model** trained on historical pollutant data and fetches live data from **OpenWeather API**.

---

## Key Features
- Instant **AQI predictions** for any city worldwide
- Interactive **Streamlit dashboard** with dropdown & manual input
- **Color-coded categories** for quick understanding
- **Gauge chart visualization** for clarity
- Session-based prediction **history tracking**
- Modern, clean, and responsive **UI**
---

## Project Preview
<p align="center">
  <img src="https://github.com/user-attachments/assets/5155dfec-9d49-4203-8625-ede995e597cf" 
       alt="AQI-Now Dashboard Preview" 
       width="80%">
</p>
<p align="center">
  <em>Clean, interactive dashboard with options to select cities or type manually and featuring real-time pollutant tables.</em>
</p>

---

## Project Structure
```
AQI-Now/
│
├─ app.py                                                   # Streamlit UI & API integration
├─ Aqi_model/
│ ├─ aqi_model.joblib                                       # Trained Random Forest ML model
│ ├─ AQI_prediction_using_Machine_Learning.ipynb            # Data processing & model training
│ ├─ city_day.csv                                           # Dataset used for training
│ └─ test_aqi_model.py                                      # Script to test the ML model
├─ requirements.txt                                         # Python dependencies
└─ README.md                                                # Project documentation
```
---

## Installation & Setup
1️. **Clone the Repository** :
```bash
git clone https://github.com/yourusername/AQI-Now.git
cd AQI-Now
```
2️. **Install Dependencies** :
```bash
pip install -r requirements.txt
```
3️. **Run the Streamlit App** :
```
streamlit run app.py
```
---

## APIs Used  
- **[OpenWeather API](https://openweathermap.org/api/air-pollution)** – Fetches real-time air pollution data  
- **[OpenCage Geocoder](https://opencagedata.com/api)** – Converts city names to coordinates  
---

## How It Works
### 1️. User Input:
- Select a **city from the dropdown** (e.g., Ahmedabad)  
- Or **type a city manually** to fetch AQI for any location worldwide 
### 2️. Fetch Live Data:
- The app fetches **real-time pollutant levels** from OpenWeather API:  
  PM2.5 | PM10 | NO | NO2 | NH3 | CO | SO2 | O3  
### 3️. AI-Powered AQI Prediction:
- A **Random Forest Machine Learning model** predicts the AQI based on current pollutant levels
- The model is trained on historical city data for accurate, real-time inference
### 4️. Results & Visualization:
- Displays the **predicted AQI value**
- Shows the **color-coded AQI category** for easy interpretation
- Interactive gauge chart for visual feedback
- Optionally compares with API AQI and shows prediction agreement %
### 5. Session History:
- **Keeps track** of all predictions made in the current session
- Users can view historical AQI predictions alongside real-time data
---

## Model Details & Evaluation
### Models Used:
The following regression models were trained to predict AQI:
1. **Linear Regression**  
2. **Random Forest Regressor** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(Best model)*
3. **Decision Tree Regressor**  
4. **Support Vector Regressor**  
5. **Gradient Boosting Regressor**  
6. **AdaBoost Regressor**  
7. **Lasso Regression**  
8. **Ridge Regression**  
9. **ElasticNet Regression**  

### Evaluation Metrics:
All models were evaluated using standard regression metrics:
1. **Mean Absolute Error (MAE)** – Average absolute difference between predicted and actual AQI  
2. **Mean Squared Error (MSE)** – Average squared difference between predicted and actual AQI  
3. **R² Score** – Coefficient of determination showing how well the model explains variance in AQI  

### Best Model:
- **Random Forest Regressor** was selected as the best-performing model based on MAE, MSE, and R² Score.  
- Trained model is exported as **`aqi_model.joblib`** for fast inference.

## Model Evaluation Results
<p align="center">
  <img src="https://github.com/user-attachments/assets/de61be5e-59b0-4e98-b18b-e2989d13cc91" alt="Model Evaluation Results" width="100%">
</p>
<p align="center"><em>Figure: Comparison of different ML models on AQI prediction (MAE, MSE, R² Score).<br>
<strong>Random Forest</strong> shows the best performance.</em></p>

---

## Example Usage
### By City Name (Dropdown or Manual Entry)
The user can obtain AQI predictions in two ways:  
1. **Select a city** from the predefined dropdown list of popular cities.  
2. **Type a city manually** in the input box if the desired city is not listed. 
**Example:** 
```
City chosen: Ahmedabad  (via dropdown or manual entry)  
Predicted AQI: 103 (Moderate)    
```
- Displays **real-time pollutant concentrations** (PM2.5, PM10, NO, NO2, NH3, CO, SO2, O3)  
- Shows **predicted AQI** with **color-coded category**  
- Includes **gauge chart visualization** for quick understanding  
- Optionally compares with **API AQI** and shows **prediction agreement %**  
---

## User Experience
- **Interactive:** Select from dropdown or type any city  
- **Visual & numeric:** See AQI numbers, color categories, and gauge chart simultaneously  
- **Real-time updates:** Pollutants and AQI fetched live from OpenWeather API  
- **Session tracking:** Keeps history of all predictions in the current session  
- **Clean & professional UI:** White background, styled buttons, readable tables, footer with credits  
- **Immediate feedback:** Warnings or errors show up if city is invalid or API fails
---

## Future Enhancements
- **Improve Model Accuracy:** Train on larger and more diverse datasets to enhance AQI predictions.  
- **Historical AQI Trends:** Include past AQI data and trend graphs for better insights over time.  
- **Real-Time Alerts & Notifications:** Notify users when AQI reaches unhealthy or hazardous levels.  
- **Advanced Visualization:** Add interactive charts, maps, and heatmaps for intuitive understanding.
---

## **Developed by Team AQI-Now**  
| Name           | IAR No.  |
|----------------|----------|
| Disha Girase   | 14099    |
| Irnitee Patel  | 14219    |
---
## Project Presentation

[View Presentation](AQI-NOW__presentation.pdf)

## Built With
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) 
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/) 
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/) 
[![joblib](https://img.shields.io/badge/joblib-0078D7?style=for-the-badge&logo=python&logoColor=white)](https://joblib.readthedocs.io/)
[![OpenWeather API](https://img.shields.io/badge/OpenWeatherAPI-1E90FF?style=for-the-badge&logo=none&logoColor=white)](https://openweathermap.org/api/air-pollution)
[![OpenCage Geocoder](https://img.shields.io/badge/OpenCage-Geocoder-F7941D?style=for-the-badge&logo=none&logoColor=white)](https://opencagedata.com/api)
[![Random Forest](https://img.shields.io/badge/RandomForest-228B22?style=for-the-badge&logo=none&logoColor=white)](https://scikit-learn.org/stable/modules/ensemble.html#forest)
 ---
 
 #### **Enjoying AQI-Now?** 
 Show your support by giving us a ⭐ on GitHub and sharing your feedback!  
 
<p align="center">© 2026 <strong>AQI-Now</strong>. All rights reserved.</p>

---
