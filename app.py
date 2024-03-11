import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Título pendiente')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

show_histogram = st.checkbox('Construir histograma') # crear una casilla de verificación para el histograma
show_scatter = st.checkbox('Construir gráfico de dispersión') # crear una casilla de verificación para el gráfico de dispersión
        
if show_histogram: # si la casilla de verificación del histograma está marcada
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="Odómetro", color_discrete_sequence=['red'])
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
       
if show_scatter: # si la casilla de verificación del gráfico de dispersión está marcada
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.scatter(car_data, x="Odómetro", y="Precio", color_discrete_sequence=['orange'])
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)