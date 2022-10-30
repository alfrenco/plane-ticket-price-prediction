import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import json
import pickle

# Load Model
with open('model_ada.pkl', 'rb') as file_1:
  model_ada = joblib.load(file_1)

def run():
    # Membuat title
    st.title('Plane Ticket Price Prediction')

    # Membuat sub header
    st.subheader('Prediction')
    # Membuat Form
    with st.form(key='form_parameters'):
        airline = st.selectbox('Airline',('Vistara', 'SpiceJet', 'AirAsia', 'GO_FIRST', 'Indigo', 'Air_India'), index=1)
        kelas = st.selectbox('Class',('Economy', 'Business'), index=1)
        source = st.selectbox('Source',('Delhi', 'Mumbai', 'Chennai', 'Hyderabad', 'Kolkata', 'Bangalore'), index=1)
        destination = st.selectbox('Destination',('Delhi', 'Mumbai', 'Chennai', 'Hyderabad', 'Kolkata', 'Bangalore'), index=1)
        stops = st.selectbox('Stops',('one', 'zero', 'two_or_more'), index=1)
        departure = st.selectbox('Departure',('Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'), index=1)
        arrival = st.selectbox('Arrival',('Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'), index=1)
        duration = st.slider('Flight Duration', 1, 50, 25)
        day_left = st.slider('Days Left Before Flight', 1, 50, 25)
        st.markdown('---')

        submitted = st.form_submit_button('Predict')

    # Membuat data inference
    data_inf = {
        'airline': airline,
        'source_city': source,
        'departure_time': departure,
        'stops': stops,
        'arrival_time': arrival,
        'destination_city': destination,
        'class': kelas,
        'duration': duration,
        'days_left': day_left
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:

            # Predict using Linear Regression
            y_pred_inf = model_ada.predict(data_inf)

            st.write('## Price = '+ str(int(y_pred_inf)))

if __name__ == '__main__':
    run()