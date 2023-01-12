"""
Modulos: Son funciones ya hechas para reutilizar ---> PYTHON MODULES INDEX
Podemos consewguir nuestros modulos del lenguaje, internet y tambien podemos crear nuestros modulos
"""
#Importamos nuestro propio modulo
import mimodulo # Importamos todo del modulo
from mimodulo import holamundo # Aqui importamos DE mimodulo LA FUNCION hola mundo
from mimodulo import *  # Aqui importamos DE mimodulo TODAS las funciones


print(mimodulo.holamundo("Ricardito Cruz")) #Aqui mandamos a llamar de nuesto modulo la funcion que tiene dentro

print(holamundo("Chanchito")) #Aqui mandamos a llamar nuestro modulo 


# MODULO DE FECHAS
import datetime 

print(datetime.date.today()) # Muestra la fecha actual

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year) 
print(fecha_completa.day) 
print(fecha_completa.month)

fecha_personalizada = fecha_completa.strftime("%d/%m/%y, %H:%M:%S")
print("Fecha personalizada",fecha_personalizada)

# Pagina para sacar fechas y toda su documentacion https://docs.python.org/3/library/datetime.html#module-datetime


# Modulo de matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print('Numero Pi: ', math.pi)
print('Redondear:', math.ceil(7.7836786)) #Redondea numeros tambien se utiliza FLOOR para redondear

import random

print("Numero aleatorio netre 10 y 50", random.randint(10, 50))