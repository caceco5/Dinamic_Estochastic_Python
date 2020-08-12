import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):  # clase base, genera un contructor con init

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self): # camina aleatoriamente entre 4 opciones
        return random.choice([
            (random.random(), random.random() * -1),
                (random.random() * -1, random.random()),
                (random.random() * -1, random.random() * -1),
                (random.random(), random.random()),
            ])
        #choice permite generar varias opciones que tienen la misma probabilidad