import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Select Page : ', ('Exploratory Data Analysis', 'Predict Price'))

if navigation == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()