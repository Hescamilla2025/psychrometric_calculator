'''Definicion de funciones para calculadora psicrometrica'''

import numpy as np

def p_atm(altura): #Input: Altura en metros
    ''' Se calcula la presion atmosferica en funcion de la altura del sitio'''
    p_atm = (101325*(1-0.0000225577*altura)**5.2559)/1000
    return p_atm


def p_sat(temperature): #Input: Temperatura del aire en °C
    ''' Se calcula la presion de saturacion en funcion de la temperatura del fluido'''
    C8 = -5800.2206
    C9 = 1.3914993
    C10 = -0.04864023
    C11 = 0.000041764768
    C12 = -0.000000014452093
    C13 = 6.5459673
    T = temperature + 273.15
    p_sat = (C8 / T) + C9 + (C10 * T) + (C11 * (T ** 2)) + (C12 * (T ** 3)) + (C13 * np.log(T))
    return np.exp(p_sat)/1000


def w_abs(temperature, humedad_relativa, altura): # Input: temperatura C, humedad %, altura m
    ''' Calculo de humedad absoluta'''
    humedad_relativa = humedad_relativa/100
    w_abs = 0.621945 * (humedad_relativa * p_sat(temperature) / (p_atm(altura) - humedad_relativa * p_sat(temperature)))
    humedad_relativa = humedad_relativa*100
    return w_abs

def w_sat(temperature, altura):
    ''' Calculo de humedad absoluta en condiciones saturadas'''
    w_sat = 0.621945 * (p_sat(temperature) / ( p_atm(altura) - p_sat(temperature)))
    return w_sat

def twb(temperature, relative_humidity, altura):
    '''Calculdora de temperatura de bulbo humedo'''
    twb_prop = temperature
    error  = 1
    delta = 0.0001
    while error > 0.005:
        w = w_abs(temperature, relative_humidity, altura)
        ws = w_sat(twb_prop, altura)
        A = 1.006 * temperature
        B = w * (2501 + 1.86 * temperature)
        C = -2501 * ws
        D = 1.006 + 1.86 * ws
        twb_calc = (A + B + C) / D
        error = np.abs(twb_prop - twb_calc)
        if twb_calc < twb_prop:
            twb_prop = twb_prop - delta
        else:
            twb_prop = twb_prop + delta
    return twb_calc

def specific_volume(temperature, relative_humidity, altura):
    w = w_abs(temperature, relative_humidity, altura)
    p = p_atm(altura)
    return 0.287042 * (temperature + 273.15) * (1 + 1.607858 * w) / p # m3 / kg

def density(specific_volume):
    return 1 / specific_volume # kg /  m3