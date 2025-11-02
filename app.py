import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load extended dataset with new symptoms!
df = pd.read_csv('data.csv')
X = df[['temperature', 'cough', 'sore_throat', 'sneezing', 'age',
        'headache', 'fatigue', 'body_ache', 'runny_nose', 'chills']]
y = df['diagnosis']

model = DecisionTreeClassifier()
model.fit(X, y)

advice = {
    "cold": "Drink warm fluids and rest.",
    "flu": "See a doctor if symptoms persist. Avoid contact with others.",
    "fever": "Monitor temperature and stay hydrated.",
    "allergy": "Avoid allergens and consult an allergist if symptoms worsen.",
    "malaria": "Seek immediate medical attention and get tested for malaria.",
    "typhoid": "Consult a doctor and avoid self-medication.",
    "no risk": "You seem healthy! Maintain good habits."
}

st.title("AI Health Diagnostics Tool (Advanced)")
st.write("Enter your symptoms below to get a prediction!")

your_temp = st.number_input("Enter your temperature (F)", min_value=95, max_value=110, value=98)
your_cough = st.radio("Do you have cough?", ("No", "Yes"))
your_throat = st.radio("Do you have a sore throat?", ("No", "Yes"))
your_sneeze = st.radio("Are you sneezing?", ("No", "Yes"))
your_age = st.number_input("Your age", min_value=0, max_value=120, value=25)
your_headache = st.radio("Do you have headache?", ("No", "Yes"))
your_fatigue = st.radio("Do you feel fatigue?", ("No", "Yes"))
your_body_ache = st.radio("Do you have body ache?", ("No", "Yes"))
your_runny_nose = st.radio("Do you have a runny nose?", ("No", "Yes"))
your_chills = st.radio("Do you have chills?", ("No", "Yes"))

cough_val = 1 if your_cough == "Yes" else 0
throat_val = 1 if your_throat == "Yes" else 0
sneeze_val = 1 if your_sneeze == "Yes" else 0
headache_val = 1 if your_headache == "Yes" else 0
fatigue_val = 1 if your_fatigue == "Yes" else 0
body_ache_val = 1 if your_body_ache == "Yes" else 0
runny_nose_val = 1 if your_runny_nose == "Yes" else 0
chills_val = 1 if your_chills == "Yes" else 0

if st.button("Get Diagnosis"):
    sample = [[your_temp, cough_val, throat_val, sneeze_val, your_age,
               headache_val, fatigue_val, body_ache_val, runny_nose_val, chills_val]]
    prediction = model.predict(sample)[0]
    st.success(f"Prediction: {prediction}")
    st.info(f"Advice: {advice.get(prediction, 'Consult a doctor!')}")