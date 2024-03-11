import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Venta de vehículos')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

show_histogram = st.checkbox('Construir histograma') # crear una casilla de verificación para el histograma
show_scatter = st.checkbox('Construir gráfico de dispersión') # crear una casilla de verificación para el gráfico de dispersión
        
if show_histogram: # si la casilla de verificación del histograma está marcada
    # escribir un mensaje
    st.write('Muestra la distribución de los odómetros de los vehículos en anuncios de venta')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", color_discrete_sequence=['orange'], labels={'odometer': 'Odómetro'})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
       
if show_scatter: # si la casilla de verificación del gráfico de dispersión está marcada
    # escribir un mensaje
    st.write('Muestra la relación entre el precio y el odómetro de los vehículos en anuncios de venta')
            
    fig = px.scatter(car_data, x="odometer", y="price", color_discrete_sequence=['orange'], labels={'odometer': 'Odómetro', 'price': 'Precio'})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)