# AQI-Now 

## Overview
**AQI-Now** is a **real-time Air Quality Index (AQI) predictor** using a trained **Random Forest ML model** and live data from the **OpenWeather API**.  
Users can enter a **city name** or **latitude & longitude**, and the app instantly predicts AQI with a **color-coded gauge chart** for easy visualization.

---

## Key Features
- **Real-time AQI prediction**  
- **Interactive Streamlit UI**  
- **Search by city name or coordinates**  
- **Color-coded AQI categories** with a gauge chart  
- **Fast ML model** for instant predictions  
- **Live air pollution data** from OpenWeather API  

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

1️. **Clone the Repository**  

```bash
git clone https://github.com/yourusername/AQI-Now.git
cd AQI-Now
```

2️. **Install Dependencies**
```bash
pip install -r requirements.txt
```
3️. **Run the Streamlit App**
```
streamlit run app.py
```

---

## APIs Used  
- **[OpenWeather API](https://openweathermap.org/api/air-pollution)** – Fetches real-time air pollution data  
- **[OpenCage Geocoder](https://opencagedata.com/api)** – Converts city names to coordinates  

---
## How It Works

### 1️. Input Data
- Enter a **city name** (e.g., Ahmedabad)  
- Or enter **latitude & longitude**  

### 2️. Fetch Live Data
- The app fetches **real-time pollutant levels** from OpenWeather API:  
  - PM2.5  
  - PM10  
  - NO  
  - NO2  
  - NH3  
  - CO  
  - SO2  
  - O3  

### 3️. Predict AQI
- The **Random Forest model** predicts AQI based on the pollutant levels  

### 4️. Display Results
- **AQI value**  
- **Color-coded category**  
- **Gauge chart** for visual representation  
- Optional **API comparison** for accuracy

## Model Details & Evaluation

### Models Used
The following regression models were trained to predict AQI:

1. **Linear Regression**  
2. **Random Forest Regressor**          (Best model)  
3. **Decision Tree Regressor**  
4. **Support Vector Regressor (SVR)**  
5. **Gradient Boosting Regressor**  
6. **AdaBoost Regressor**  
7. **Lasso Regression**  
8. **Ridge Regression**  
9. **ElasticNet Regression**  

### Evaluation Metrics
All models were evaluated using standard regression metrics:

1. **Mean Absolute Error (MAE)** – Average absolute difference between predicted and actual AQI  
2. **Mean Squared Error (MSE)** – Average squared difference between predicted and actual AQI  
3. **R² Score** – Coefficient of determination showing how well the model explains variance in AQI  

### Best Model
- **Random Forest Regressor** was selected as the best-performing model based on MAE, MSE, and R² Score.  
- Trained model is exported as **`aqi_model.joblib`** for fast inference.

## Model Evaluation Results

<p align="center">
  <img src="https://github.com/user-attachments/assets/de61be5e-59b0-4e98-b18b-e2989d13cc91" alt="Model Evaluation Results" width="100%">
</p>

<p align="center"><em>Figure: Comparison of different ML models on AQI prediction (MAE, MSE, R² Score).<br>
<strong>Random Forest</strong> shows the best performance.</em></p>

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

## User Experience

- **Interactive:** Select from dropdown or type any city  
- **Visual & numeric:** See AQI numbers, color categories, and gauge chart simultaneously  
- **Real-time updates:** Pollutants and AQI fetched live from OpenWeather API  
- **Session tracking:** Keeps history of all predictions in the current session  
- **Clean & professional UI:** White background, styled buttons, readable tables, footer with credits  
- **Immediate feedback:** Warnings or errors show up if city is invalid or API fails

## Future Enhancements

- **Improve Model Accuracy:** Train on larger and more diverse datasets to enhance AQI predictions.  
- **Historical AQI Trends:** Include past AQI data and trend graphs for better insights over time.  
- **Real-Time Alerts & Notifications:** Notify users when AQI reaches unhealthy or hazardous levels.  
- **Advanced Visualization:** Add interactive charts, maps, and heatmaps for intuitive understanding.

## Team Members

| Name           | IAR No.  |
|----------------|----------|
| Disha Girase   | 14099    |
| Irnitee Patel  | 14219    |

---

⭐ Enjoying AQI-Now? Give it a star on GitHub and share your feedback!  

Built with ❤️ using Streamlit, OpenWeather API, and a Random Forest ML model.  

© 2026 AQI-Now Project. All rights reserved.  
