import random
import math


def media(X):
    return sum(X) / len (X) #formula de la media


def varianza(X):
    mu = media(X) #resultado de la media y la guarda en la variable mu.

    acumulador = 0 #variable que inicia en cero.
    
    for x in X: # for 
        acumulador += (x - mu)**2 # a cada valor de "acumulador", sumarle valor(X) - mu elevado al 2.
    
    return acumulador / len(X) #devuelve el resultado de acumulador / el total de elementos.

def desviacion_estandar(X):
    return math.sqrt(varianza(X))


if __name__ == "__main__":
    X = [random.randint(8, 13) for i in range(20)] #se introducen los valores de X, de 1 a 20
    mu = media(X) #Realiza la operacion en la funcion media y la guarda en la variable mu.
    Var = varianza(X)
    Sigma = desviacion_estandar(X)

    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion estandar = {Sigma}')