import streamlit as st
import pandas as pd
import pickle

st.write("""
# Online Food feedback prediction
This app predicts the **Feedback for the Online Foods** type!
""")

st.sidebar.header('Input')
def user_input_features():
    Age = st. sidebar.slider('Age', 0, 100, 22)
    Gender = st. sidebar.selectbox('Gender', ['Male', 'Female'])
    MaritalStatus = st.sidebar.selectbox('Marital Status', ['Single', 'Married'])
    Occupation = st. sidebar.selectbox('Occupation', ['Student',' Employee'])
    MonthlyIncome = st. sidebar.selectbox('Monthly Income', ['No Income', '10001 to 25000', '25001 to 50000',' Below Rs.10000'])
    EducationalQualifications = st. sidebar.selectbox('Educational Qualifications', ['Post Graduate', 'Graduate'])
    FamilySize = st.sidebar.slider('Family Size', 0, 100, 22)
    Output = st. sidebar.selectbox('Output', ['Yes', 'No'])
    data = {'Age': Age,
            'Gender': Gender,
            'Marital Status': MaritalStatus,
            'Occupation': Occupation,
            'Monthly Income': MonthlyIncome,
            'Educational Qualifications' : EducationalQualifications,
            'Family size':FamilySize,
            'Output': Output}


    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
# Encode labels in column 'species'.
df['Gender']= label_encoder.fit_transform(df['Gender'])
df['Marital Status']= label_encoder.fit_transform(df['Marital Status'])
df['Occupation']= label_encoder.fit_transform(df['Occupation'])
df['Monthly Income']= label_encoder.fit_transform(df['Monthly Income'])
df['Educational Qualifications']= label_encoder.fit_transform(df['Educational Qualifications'])
df['Output']= label_encoder.fit_transform(df['Output'])


loaded_model = pickle.load(open("onlinefoods.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader(' Feedback Prediction')
st.write(prediction)
