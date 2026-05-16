# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:01:44 2026

@author: AjayGangwar
"""


import pandas as pd
import pickle
import streamlit as st

# Loading the trained model
model_path = "trained_model.sav"
loaded_model = pickle.load(open(model_path, "rb"))

input_data=(5,166,72,19,175,25.8,0.587,51)

def diabetes_predication(input_data):
    feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    # Create a DataFrame with the same feature names as the training data to avoid warnings
    input_data_df = pd.DataFrame([input_data], columns=feature_names)

    prediction = loaded_model.predict(input_data_df)

    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"
    
    
def main():
    # Page configuration
    st.set_page_config(page_title="Diabetes Prediction System", page_icon="🏥", layout="centered")

    # Give a title 
    st.title("🏥 Diabetes Prediction System")
    st.markdown("---")
    
    # Use columns for a better layout
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('🤰 Number of Pregnancies', placeholder="e.g. 1")
        BloodPressure = st.text_input("💓 Blood Pressure Value", placeholder="e.g. 80")
        Insulin = st.text_input("💉 Insulin Level", placeholder="e.g. 0")
        DiabetesPedigreeFunction = st.text_input("🧬 Diabetes Pedigree Function", placeholder="e.g. 0.47")

    with col2:
        Glucose = st.text_input("🩸 Glucose Level", placeholder="e.g. 120")
        SkinThickness = st.text_input("📏 Skin Thickness Value", placeholder="e.g. 20")
        BMI = st.text_input("⚖️ BMI Value", placeholder="e.g. 22.5")
        Age = st.text_input("📅 Age of the person", placeholder="e.g. 33")
    
    # Code for prediction
    diagnosis = ""
    
    # Creating a button for prediction
    if st.button("🔍 Diabetes Test Result"):
        try:
            # Convert inputs to float
            user_input = [
                float(Pregnancies), float(Glucose), float(BloodPressure), 
                float(SkinThickness), float(Insulin), float(BMI), 
                float(DiabetesPedigreeFunction), float(Age)
            ]
            diagnosis = diabetes_predication(user_input)
            
            if "not diabetic" in diagnosis:
                st.success(f"✅ {diagnosis}")
            else:
                st.error(f"⚠️ {diagnosis}")
        except ValueError:
            st.warning("⚠️ Please enter valid numeric values for all fields.")


if __name__=="__main__":
    main()
  