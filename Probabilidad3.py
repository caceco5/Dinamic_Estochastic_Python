import random

def tirar_dado(numero_de_tiros): #definir funcion tirar dado con el numero de tiros como parametro.
    secuencia_de_tiros = [] #variable auxiliar secuencia de tiros

    for _ in range(numero_de_tiros): #se genera un for loop tantos tiros nos diga el parametro. 
        tiro = random.choice([1, 2, 3, 4, 5, 6]) #un tiro definido con random choice entre los numeros de 1 hasta 6
        secuencia_de_tiros.append(tiro) #luego se anade tiro a la secuencia de tiros.

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = [] # este es un arreglo vacio donde se van a guardar todas las veces que se corra la simulacion.
    for _ in range(numero_de_intentos): # generar un loop que corra el numero de intentos que nosotros definimos. 
        secuencia_de_tiros = tirar_dado(numero_de_tiros) #cuantos tiros queremos realizar para que genere una secuencia de tiros. ]
                                                        #si se tira el dado 10 veces la secuencia tendra 10 valores.
        tiros.append(secuencia_de_tiros) #se añade esta secuencia a tiros.

    tiros_con_1 = 0 #probabilidad sencilla.
    for tiro in tiros: #para cada tiro en tiros
        if 1 not in tiro: #si hay un 1 
            tiros_con_1 += 1 #se anade un uno a la cuentas de unos.
    
    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos #formula de la estadistica.
    
    print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1} ')
        

if __name__ == "__main__":
    numero_de_tiros = int(input('Cuantos tiros del dado: ')) #Cuantas veces queremos simular la tirada del dado.
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: ')) #Número de intentos de la simulación.

    main(numero_de_tiros, numero_de_intentos)
