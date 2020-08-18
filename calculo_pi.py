

import random
import math
from estadistica import desviacion_estandar, media

def aventar_agujas(numero_de_agujas): #funcion aventar agujas que recibe un parametro (numero de agujas), es decir cuantas agujas se van a aventar
    adentro_del_circulo = 0 #variable cuantas cayeron dentro del circulo

    for _ in range(numero_de_agujas): # se simula el numero de agujas con el numero disponible de agujas.
        x = random.random() * random.choice([-1, 1]) #coordenada entre -1 y 1 multiplicado por un choice.
        y = random.random() * random.choice([-1, 1]) #coordenada entre -1 y 1 multiplicado por un choice.
        distancia_desde_el_centro = math.sqrt(x**2 + y**2) #distancia desde el centro, raiz cuadrada

        if distancia_desde_el_centro <= 1: #si la distancia <= 1 esta adentro sino esta afuera
            adentro_del_circulo += 1 #contar

    return (4 * adentro_del_circulo) / numero_de_agujas #regresa la stimacion de Pi


def estimacion(numero_de_agujas, numero_de_intentos): #cuantas veces se van a correr la simulación
    estimados = [] #variable de todas las estimacion de pi
    for _ in range(numero_de_intentos): #for loop, que corre # de intentos
        estimacion_pi = aventar_agujas(numero_de_agujas) 
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimados, 5)}, sigma={round(sigma, 5)}, agujas={numero_de_agujas}')

    return (media_estimados, sigma) #Regresa una tubla

def estimar_pi(precision, numero_de_intentos): #
    numero_de_agujas = 1000 #numerod e agujas para empezar
    sigma = precision # aqui inicia la desviacion estandar en la precision.

    while sigma >= precision / 1.96: # aqui 95% grado confiabilidad.  
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos) #obtenemos media y sigma, llamamos estimacion y metemos los parametros
        numero_de_agujas *= 2 #multiplicar agujas por 2 para ir volviendo la distribucion normal mas pequeña para disminuir la dispersión.

    return media #genere el valor media

if __name__ == '__main__':
    estimar_pi(0.01, 1000) #precision del 0.01 con 1000 intentos 
