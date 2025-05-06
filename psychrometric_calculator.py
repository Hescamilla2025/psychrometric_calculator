''' Streamlit aplicacion para calculos psicrometricos instantaneos'''

import streamlit as st
import numpy as np
from functions import p_atm, p_sat, w_abs, w_sat, twb, specific_volume, density

#Titulo
st.title('Calculadora psicrometrica simple')


#Slider de altura
altura = st.slider('Altura del area de trabajo (m)', 0 , 5000)


#Calculo de presion atmosferica
st.text(f'Presion atmosferica: {round(p_atm(altura),2)} kPa')


#Slider de temperatura y humedad relativa
temperature = st.slider('Temperatura del aire (°C)', 0, 100)
relative_humidity = st.slider('Humedad relativa del aire (%)', 0, 100)


#Calculo de presion de saturacion, humedad absoluta, humedad absoluta saturada y temperatura de bulbo humedo
st.text(f'Presion de saturacion del agua: {round(p_sat(temperature),2)} kPa')
st.text(f'Humedad absoluta: {round(w_abs(temperature, relative_humidity, altura),4)} kg / Kgda')
st.text(f'Humedad absoluta saturada: {round(w_sat(temperature, altura),4)} kg / Kgda')
st.text(f'Temperatura de bulbo humedo: {round(twb(temperature, relative_humidity, altura),2)} °C')
st.text(f'Volumen especifico: {round(specific_volume(temperature, relative_humidity, altura),2)} m3 / kg')
st.text(f'Densidad: {round(density(specific_volume(temperature, relative_humidity, altura)),2)} kg / m3')
