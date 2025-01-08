import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
from sklearn.preprocessing import StandardScaler


# Set page configuration
st.set_page_config(
    page_title="Prediction of Disease Outbreaks",
    layout="wide",
    page_icon="💪"
)

# Custom CSS for beautification
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        font-family: Arial, sans-serif;
    }
    .main-title {
        color: #2c3e50;
        text-align: center;
        padding: 20px;
    }
    .sub-title {
        color: #34495e;
        text-align: center;
        margin-bottom: 30px;
    }
    .prediction-result {
        font-size: 1.2em;
        color: white;
        background-color: #3498db;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page header
st.markdown("<h1 class='main-title'>Prediction of Disease Outbreaks</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='sub-title'>A user-friendly app to predict diabetes, heart disease, and Parkinson's disease using machine learning.</p>",
    unsafe_allow_html=True
)

# Getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/Models/parkinsons_model.sav', 'rb'))

# Navigation menu
with st.sidebar:
    selected = option_menu(
        "Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0
    )


# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.header("Diabetes Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    with col2:
        Glucose = st.slider("Glucose Level", 0, 200, 100)
    with col3:
        BloodPressure = st.slider("Blood Pressure", 0, 140, 80)

    with col1:
        SkinThickness = st.slider("Skin Thickness", 0, 100, 20)
    with col2:
        Insulin = st.slider("Insulin Level", 0, 900, 150)
    with col3:
        BMI = st.number_input("BMI", min_value=0.0, max_value=60.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01)
    with col2:
        Age = st.slider("Age", 0, 120, 25)

    if st.button("Get Diabetes Test Result"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        prediction = diabetes_model.predict([user_input])
        result = "The person is diabetic." if prediction[0] == 1 else "The person is not diabetic."
        st.markdown(f"<div class='prediction-result'>{result}</div>", unsafe_allow_html=True)

# Heart Disease Prediction Page
elif selected == "Heart Disease Prediction":
    st.header("Heart Disease Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 0, 120, 50)
    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"])
    with col3:
        cp = st.selectbox("Chest Pain Types", ["Type 1", "Type 2", "Type 3", "Type 4"])

    with col1:
        trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)
    with col2:
        chol = st.slider("Serum Cholestoral (mg/dl)", 100, 400, 200)
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])

    with col1:
        restecg = st.slider("Resting ECG Results", 0, 2, 1)
    with col2:
        thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150)
    with col3:
        exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])

    with col1:
        oldpeak = st.slider("ST Depression Induced by Exercise", 0.0, 6.0, 1.0, step=0.1)
    with col2:
        slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    with col3:
        ca = st.slider("Number of Major Vessels Colored by Fluoroscopy", 0, 4, 0)
    with col1:
        thal = st.selectbox("Thallium stress", ["Normal","Fixed Defect","Reversable Defect"])

    if st.button("Get Heart Disease Test Result"):
        user_input = [
            1 if sex == "Male" else 0,
            0 if cp == "Type 1" else 1 if cp == "Type 2" else 2 if cp == "Type 3" else 3,
            1 if fbs == "Yes" else 0,
            restecg,
            1 if exang == "Yes" else 0,
            0 if slope=='Upsloping' else 1 if slope=='Flat' else 3,
            ca,
            0 if thal == 'Normal' else 1 if thal =='Fixed Defect' else 2,
            age,
            trestbps,
            chol,
            thalach,
            oldpeak
        ]
        prediction = heart_disease_model.predict([user_input])
        result = "The person has heart disease." if prediction[0] == 1 else "The person does not have heart disease."
        st.markdown(f"<div class='prediction-result'>{result}</div>", unsafe_allow_html=True)
elif selected == "Parkinson's Prediction":
    st.header("Parkinson's Disease Prediction")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0, step=0.1)
    with col2:
        fhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0, step=0.1)
    with col3:
        flo = st.number_input("MDVP:Flo(Hz)", min_value=0.0, step=0.1)
    with col4:
        Jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0, step=0.001)
    with col5:
        Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, step=0.0001)

    with col1:
        RAP = st.number_input("MDVP:RAP", min_value=0.0, step=0.0001)
    with col2:
        PPQ = st.number_input("MDVP:PPQ", min_value=0.0, step=0.0001)
    with col3:
        DDP = st.number_input("Jitter:DDP", min_value=0.0, step=0.0001)
    with col4:
        Shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, step=0.0001)
    with col5:
        Shimmer_dB = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, step=0.001)
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    if st.button("Get Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        prediction = parkinsons_model.predict([user_input])
        result = "The person has Parkinson's disease." if prediction[0] == 1 else "The person does not have Parkinson's disease."
        st.markdown(f"<div class='prediction-result'>{result}</div>", unsafe_allow_html=True)
    