import streamlit as st
import pandas as pd
import pickle


st.write("""
# Online Food feedback prediction
This app predicts the **Feedback for the Online Foods** type!
""")


st.sidebar.header('Input')
def user_input_features():
    Age = st. sidebar.slider('Age', 18, 33, 15)
    Gender = st. sidebar.selectbox('Gender', ['Male', 'Female'])
    MaritalStatus = st.sidebar.selectbox('Marital Status', ['Single', 'Married','Prefer not to say'])
    Occupation = st. sidebar.selectbox('Occupation', ['Student',' Employee','House wife','Self Employeed'])
    MonthlyIncome = st. sidebar.selectbox('Monthly Income', ['No Income', '10001 to 25000', '25001 to 50000',' Below Rs.10000','More than 50000',])
    EducationalQualifications = st. sidebar.selectbox('Educational Qualifications', ['Post Graduate', 'Graduate','Ph.D','School','Uneducated'])
    FamilySize = st.sidebar.slider('Family Size', 1, 6, 2)
    Output = st. sidebar.selectbox('Output', ['Yes', 'No'])
    data = {'Age': Age,
            'Gender': Gender,
            'Marital Status': MaritalStatus,
            'Occupation': Occupation,
            'Monthly Income': MonthlyIncome,
            'Educational Qualifications' : EducationalQualifications,
            'Family size':Family size,
            'Output': Output}


    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()
