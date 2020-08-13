import random
import collections

PALOS = ['espada',  'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']


def crear_baraja(): #funcion 
    barajas = [] #lista que va a tener todas las barajas
    for palo in PALOS: #loop
        for valor in VALORES: #loop
            barajas.append((palo, valor)) #se le da append a una tuple

    return barajas

def obtener_mano(barajas, tamano_mano): #Recibe las barajas y el tamano de la mano
    mano = random.sample(barajas, tamano_mano) #randomsanmple: se obtiene una muestra por turno. no repite lo que ya salio.
    
    return mano

def main(tamano_mano, intentos): #recibe el tamano de la mano y los intentos de simulacion.
    barajas = crear_baraja() #se crea una baraja

    manos = []  #variable que guarda todas las manos que se van a obtener en la simulacion
    for _ in range(intentos):   #se corre la simulacion tantas veces como dijo el usuario.
        mano = obtener_mano(barajas, tamano_mano)   
        manos.append(mano)  #se le a;ade a manos la mano que se obtuvo previamente.

    pares = 0   #variable pares para calcular su probabilidad.
    for mano in manos:  
        valores = [] # se guardan los valores en un array.
        for carta in mano: #por cada carta en la mano
            valores.append(carta[1]) #es indice 1 porque en linea 11, el palo es el indice 0 y el valor es el indice 1.

        counter = dict(collections.Counter(valores)) #contador, se usa la clase counter de collections, para los valores. note que se vuelve un DICCIONARIO
        for val in counter.values(): #por cada valor en el counter values, se puede acceder con values porque ahora es un DICCIONARIO
            if val == 3: # ES EL PARAMETRO DE BUSQUEDA EN ESTE CASO PAR
                pares += 1
                break #probabilidad de encontrar un solo par.
        # print(counter)
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)