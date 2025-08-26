# myfile.py

import streamlit as st
import pickle

# Load the trained model
with open("project.pkl", "rb") as f:
    model = pickle.load(f)

# Title of the app
st.title("Titanic Survival Prediction")

# User inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
age = st.slider("Age of Passenger", 1, 100, 25)
gender = st.selectbox("Gender", ["Male", "Female"])

# Convert gender to numerical
gender_val = 1 if gender == "Male" else 0

# Predict button
if st.button("Predict"):
    result = model.predict([[pclass, age, gender_val]])[0]
    if result == 1:
        st.success("🎉 The passenger would have SURVIVED!")
    else:
        st.error("❌ The passenger would NOT have survived.")
