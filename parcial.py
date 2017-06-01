
import random

import  numpy as np

class Algoritmo_genetico(object):
    """docstring for Algoritmo_genetico."""
    def __init__(self, individuo_modelo, poblacion_inicial):
        # Modelo de cromosoma, es decir el objetivo que se pretende alcanzar con el algoritmo.
        self.individuo_modelo = individuo_modelo
        # Longitud del tamano genetico del cromosoma
        self.genes = len(individuo_modelo)
        # Cantidad de individuos que se selecciona para la mutacion
        self.poblacion_inicial = poblacion_inicial
        # Poblacion general
        self.poblacion = self.generarPoblacion()
        # Resultado de la funcion fitness para cada individuo de la poblacion
        self.resultado_fitness = []

        print("individuo_modelo {}, genes {} ").format(self.individuo_modelo, self.genes)
        print(self.individual())
        print(self.poblacion)
        self.calcularFitness()
        print("\n")

    """Crea un individuo aleatorio dentro del rango del numero de genes del individuo modelo."""
    def individual(self, min = 0, max = 1):
            return[random.randint(min, max) for i in range(self.genes)]

    """Genera una poblacion de individuos aleatoria."""
    def generarPoblacion(self):
        return [self.individual() for i in range(self.poblacion_inicial)]

    """Calcula el valor del fitness para cada individuo de la poblacion."""
    def calcularFitness(self):
        for i in range(len(self.poblacion)):
            res_fitness = 0
            fitness = self.poblacion[i]
            for j in range(len(fitness)):
                res_fitness = res_fitness + abs(self.individuo_modelo[j] - fitness[j])
            print(-res_fitness)
            res = 0

if __name__ == "__main__":

    individuo_modelo = np.array([1, 1, 0, 1, 0, 0, 1, 0])
    poblacion_inicial = 4

    genetico = Algoritmo_genetico(individuo_modelo, poblacion_inicial);
