import random


def media(X):
    return sum(X) / len (X) #formula de la media

if __name__ == "__main__":
    X = [random.randint(1, 21) for i in range(20)] #se introducen los valores de X, de 1 a 20
    mu = media(X) #Realiza la operacion en la funcion media y la guarda en la variable mu.

    print(X)
    print(mu)