# Disease-Outbreak-Project
This application is a user-friendly web interface for predicting the likelihood of three major diseases: Diabetes, Heart Disease, and Parkinson's Disease. It leverages machine learning models trained on relevant datasets to provide health predictions based on user input.

# Features
1. Diabetes Prediction:
* Input parameters: Number of pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age.
* Model output: Predicts whether the individual is diabetic or not.

2. Heart Disease Prediction:
* Input parameters: Age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, ECG results, max heart rate, exercise-induced angina, and more.
* Model output: Predicts the presence or absence of heart disease.

3. Parkinson's Disease Prediction:
* Input parameters: A range of vocal metrics (e.g., MDVP features, jitter, shimmer, NHR, etc.).
* Model output: Predicts whether the individual has Parkinson's disease.

# Technologies Used
* Framework: Streamlit
* Language: Python
* Machine Learning: Scikit-learn
* Models: Pre-trained models loaded via pickle.

# Installation and Setup
- Step 1: Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
- Step 2: Install dependencies:
    - Make Sure you have already installed all the required dependencies.
- Step 3: Ensure the Models directory is populated:
   - Place pre-trained models (diabetes_model.sav, heart_disease_model.sav, parkinsons_model.sav) in the Models directory.
- Step 4: Run the application:
    ```bash
   - streamlit run app.py

# Usage
1. Launch the app in your browser using the above command.
2. Navigate through the sidebar to select the prediction type:
  - Diabetes
  - Heart Disease
  - Parkinson's Disease
3. Fill in the required input fields for the chosen disease.
4. Click the "Get Test Result" button to view the prediction.

# File Structure
- app.py: Main application script.
- Models/: Directory for storing pre-trained machine learning models.
- Datasets/: Directory for all the required datasets
