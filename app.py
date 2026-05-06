import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de Anuncios de Venta de Coches')

build_histogram = st.checkbox('Mostrar histograma de odómetro')

if build_histogram:
    st.write('Histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Mostrar gráfico de dispersión precio vs odómetro')

if build_scatter:
    st.write('Gráfico de dispersión: precio vs odómetro')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)