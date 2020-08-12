
from camino_de_borrachos import BorrachoTradicional #importacion de clases.
from campo import Campo #campo es el modulo y Campo es la clase.
from coordenada import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho) #cual es el inicio, nos  debe dar al inicio (0, 0)

    for _ in range(pasos): #para el rango de los pasos, tantos pasos se diga
        # de campo con la funcion mover borracho, se le entrega como parametro un borracho.
        campo.mover_borracho(borracho)
        #le decimos a la coordenada de inicio 

    return inicio.distancia(campo.obtener_coordenada(borracho)), campo.obtener_coordenada(borracho)

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    #llamada a tipo de borracho, a diferencia de llamarlo directamente como borracho tradicional, se lo recibe como parametro de la funcion
    # lo que se hace es inicializar una instancia de borracho tradicional o de cualquier tipo de borracho que se le mande.
    # "agnostica" recibe un borracho, cualquie tipo.
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancia = []  #variable que guarda las distancias en cada una de las simulaciones.
    coordenada = []
    """por cada intento, el _ indica que no utilizaremos variable """
    for _ in range(numero_de_intentos):
        campo = Campo()  #simulacion 
        campo.anadir_borracho(borracho, origen) #se añade un borracho y un origen de coords
        simulacion_caminata, simulacion_coordenadas = caminata(campo, borracho, pasos)  #resultado de la funcion caminata, (todavia no esta implementada)
        distancia.append(round(simulacion_caminata, 1)) # que no tenga decimal
        coordenada.append((simulacion_coordenadas.x, simulacion_coordenadas.y))


    return distancia, coordenada

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    
    grafica.line(x, y, legend='distancia media')

    show(grafica)

""" definicion de main """

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    # distancias_media_por_caminata = []

    coordenada_x = []
    coordenada_y = []

    for pasos in distancias_de_caminata: #recuerde que son 10, 100, 1000, 10000
        distancias, coordenada = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)  #esto es lo que va a estar haciendo la simulacion.          
        distancia_media = round(sum(distancias) / len(distancias), 4) # obtener solo 3 decimales        
        distancia_maxima = max(distancias) #el dato maximo de la distancia
        distancia_minima = min(distancias)
        # distancias_media_por_caminata.append(distancia_media)
       
        # distancias_media_por_caminata.append(distancia_media)
        # coordenada_x.append(coordenada.x)
        # coordenada_x.append(coordenada.y)

        for x in coordenada:
            coordenada_x.append(x[0])
            coordenada_y.append(x[1])
  
       
       
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos ')
        print(f'Media = {distancia_media}') 
        print(f'Max = {distancia_maxima}') 
        print(f'Min = {distancia_minima}')
    # graficar(distancias_de_caminata, distancias_media_por_caminata)
    graficar(coordenada_x, coordenada_y)

# def main(distancia, inicio, borracho):
#     campo = Campo()
#     campo.anadir_borracho(borracho, inicio) #poner un borracho en origen
#     ejecutar_caminata(campo, borracho, distancia)


if __name__ == '__main__': #End point
    distancias_de_caminata = [10, 1000, 10000] #simulacion de 10 pasos, 100 pasos, ... ,
    numero_de_intentos = 50 #las simulaciones se corren varias veces para obtener su media.

    """ recibir classe de borracho, en vez inizializar la clase la vamos a ponerlo como referencia """

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

