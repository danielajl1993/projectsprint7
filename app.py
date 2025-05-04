import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Visualización de Data - Mayo 2018 a Marzo 2019')

car_data = pd.read_csv('C:/Users/danie/projectsprint7-1/vehicles_us.csv')

model_counts = car_data['model'].value_counts()

low_volume_models = model_counts[model_counts < 1000].index

filtered_data = car_data[car_data['model'].isin(low_volume_models)]

st.write('Modelos con menos de 1000 anuncios:')
st.dataframe(filtered_data)

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de Histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, 
                   x='model_year', 
                   color='condition', 
                   barmode='group',
                   title='Condición de autos por año del modelo',
                   labels={'model_year': 'Año del modelo', 'count': 'Cantidad de autos'})

    st.plotly_chart(fig, use_container_width=False)

build_scatter = st.checkbox('Construir diagrama de dispersión')

if build_scatter:
    st.write('Creación de gráfico de dispersión para el conjunto de datos de ventas de coches')

    fig = px.scatter(car_data, x='odometer', y='price', color='condition', title='Precio vs Kilometraje')

    st.plotly_chart(fig, use_container_width=True)