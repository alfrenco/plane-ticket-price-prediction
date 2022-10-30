import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def run():
    # Membuat title
    st.title('Plane Ticket Price Prediction')

    # Membuat sub header
    st.subheader('Exploratory Data Analysis')

    # Membuat garis lurus
    st.markdown('---')

    # Show dataframe
    data = pd.read_csv('https://raw.githubusercontent.com/alfrenco/file_milestone/main/Clean_Dataset.csv')
    data.drop(columns=['Unnamed: 0'], inplace=True)
    st.dataframe(data)

    # Airline EDA
    st.write('#### Airline')
    fig = plt.figure(figsize=(15,5))
    plt.subplot(1, 2, 1)
    sns.set_theme(style="whitegrid")
    #colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#a7fc00','#ffa343']
    sns.barplot(x='airline',y='price',data=data, palette='Dark2')
    plt.title('Airline Price')

    plt.subplot(1, 2, 2)
    data['airline'].value_counts().plot(kind='pie', explode=[0.05, 0, 0, 0 ,0 ,0], autopct='%1.1f%%', cmap='Dark2')
    plt.title('Airline Percentage')
    st.pyplot(fig)


    # City EDA
    st.write('#### Cities')
    opt = st.selectbox('Select : ',('source_city', 'destination_city'))
    fig = plt.figure(figsize=(10,5))
    data[opt].value_counts().plot(kind='pie', explode=[0.05, 0, 0, 0 ,0 ,0], autopct='%1.1f%%', cmap='Dark2')
    st.pyplot(fig)

    # Time EDA
    st.write('#### Departure and Arrival Time')
    opt = st.selectbox('Select : ',('departure_time', 'arrival_time'))
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x=opt, data=data, palette='Dark2')
    sns.set_theme(style="whitegrid")
    st.pyplot(fig)    

    # Class EDA
    st.write('#### Class')
    fig = plt.figure(figsize=(15, 5))
    sns.barplot(x='airline',y='price', hue='class' ,data=data, palette='Dark2')
    plt.title('Airline Price Per Class')
    st.pyplot(fig)

    # Days Left EDA
    st.write('#### Days Left')
    fig = plt.figure(figsize=(10,5))
    dl = data.groupby(['days_left'])['price'].mean().reset_index()
    sns.lineplot(x='days_left', y='price', data = dl)
    plt.title('Days Left Price Mean')
    st.pyplot(fig)

    # Membuat garis lurus
    st.markdown('---')
    st.write('')
    st.write('')
    
    # Membuat deskripsi
    st.write('Page by *Immanuel Yosia*')

    # Membuat garis lurus
    st.markdown('---')

if __name__ == '__main__':
    run()