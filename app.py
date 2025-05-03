import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Data Viewer')
st.write('Include manufacturers with less than 1000 ads')

car_data = pd.read_csv('C:/Users/danie/projectsprint7-1/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de Histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x= "odometer")

    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir diagrama de dispersión')

if disp_button:
    st.write('Creación de gráfico de dispersión para el conjunto de datos de ventas de coches')

    fig = px.histogram(car_data, x= "odometer")

    st.plotly_chart(fig, use_container_width=True)

