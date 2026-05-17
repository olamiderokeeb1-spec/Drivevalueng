# app.py — DriveValue Nigeria 🇳🇬 Car Price Predictor

```python
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="DriveValue Nigeria",
    page_icon="🚗",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .stApp {
        background: linear-gradient(to right, #0f172a, #1e293b);
    }

    h1, h2, h3, p, label {
        color: white !important;
    }

    .prediction-box {
        background-color: #16a34a;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: white;
        margin-top: 20px;
    }

    .small-text {
        color: #cbd5e1;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# LOAD MODEL
# =========================
@st.cache_resource

def load_model():
    model = joblib.load("car_price_model(2).joblib")
    return model

model = load_model()

# =========================
# TITLE
# =========================
st.title("🚗 DriveValue Nigeria")
st.subheader("Predict Nigerian Used Car Prices Instantly")

st.markdown(
    "<p class='small-text'>Enter your car details below to estimate the market value in Nigeria.</p>",
    unsafe_allow_html=True
)

# =========================
# INPUT SECTION
# =========================
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox(
        "Car Brand",
        [
            "Toyota", "Honda", "Lexus", "Mercedes-Benz", "BMW",
            "Hyundai", "Kia", "Ford", "Nissan", "Peugeot"
        ]
    )

    model_name = st.text_input("Car Model", "Camry")

    year = st.slider("Year", 1995, 2026, 2018)

    mileage = st.number_input("Mileage (KM)", 0, 500000, 85000)

with col2:
    transmission = st.selectbox(
        "Transmission",
        ["Automatic", "Manual"]
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "Hybrid"]
    )

    engine_size = st.number_input("Engine Size", 0.8, 8.0, 2.5)

    condition = st.selectbox(
        "Condition",
        ["Foreign Used", "Nigerian Used", "Brand New"]
    )

# =========================
# PREDICT BUTTON
# =========================
if st.button("Predict Price"):

    try:
        # Create input dataframe
        input_data = pd.DataFrame({
            "brand": [brand],
            "model": [model_name],
            "year": [year],
            "mileage": [mileage],
            "transmission": [transmission],
            "fuel_type": [fuel_type],
            "engine_size": [engine_size],
            "condition": [condition]
        })

        # Predict
        prediction = model.predict(input_data)[0]

        # Format prediction
        formatted_price = f"₦{prediction:,.0f}"

        st.markdown(
            f"""
            <div class='prediction-box'>
                Estimated Price: {formatted_price}
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Error during prediction: {e}")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("DriveValue Nigeria • AI Powered Car Price Prediction")
