import streamlit as st
import joblib

# Title of the app
st.title('Simple Streamlit App')

# select gender
gender_options = ['0 - Male', '1 - Female']
selected_gender = st.selectbox('Select patient gender:', gender_options)

# select age
selected_age = st.number_input('Enter patient age:', min_value=1, max_value=120, value=0, step=1)

# map categorical value
patient_gender = 0 if gender_options == '0 - Male' else 1;

# Display the selected options
st.write('Patient gender:', selected_gender)
st.write('Patient age:', selected_age)
