
import streamlit as st
import pickle
import numpy as np

# Load model and features
with open('calories_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('features.pkl', 'rb') as f:
    feature_names = pickle.load(f)

# --- Page Config ---
st.set_page_config(page_title="Calories Burnt Predictor", page_icon="🏋️", layout="centered")

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏋️ Calories Burnt Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Estimate how many calories you burn during workouts!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Form Inputs ---
with st.form("calories_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.number_input("Age", min_value=10, max_value=100, value=25)
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)

    with col2:
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        duration = st.number_input("Duration (min)", min_value=1, max_value=300, value=30)
        heart_rate = st.number_input("Heart Rate", min_value=50, max_value=200, value=100)

    body_temp = st.slider("Body Temperature (°C)", 30.0, 45.0, 37.0)

    submitted = st.form_submit_button("🎯 Predict Calories")

# --- Feature Engineering and Prediction ---
if submitted:
    gender_val = 1 if gender == "Male" else 0
    bmi = weight / ((height / 100) ** 2)
    effort = heart_rate * duration

    input_data = np.array([[gender_val, age, height, weight, duration,
                            heart_rate, body_temp, bmi, effort]])

    prediction = model.predict(input_data)[0]

    # --- Output ---
    st.markdown("---")
    st.success(f"✅ Estimated Calories Burnt: **{prediction:.2f} kcal**")
    st.balloons()
    st.markdown("<p style='text-align: center; font-size: 16px;'>💪 Keep pushing your limits and stay fit!</p>", unsafe_allow_html=True)
