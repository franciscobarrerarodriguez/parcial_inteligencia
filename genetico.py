from builtins import print
from operator import itemgetter, attrgetter
import random
import  numpy as np
from pip.utils import read_text_file


class Algoritmo_genetico(object):
    """docstring for Algoritmo_genetico."""
    def __init__(self, individuo_modelo, poblacion_inicial, constante_por_generacion):
        # Modelo de cromosoma, es decir el objetivo que se pretende alcanzar con el algoritmo.
        self.individuo_modelo = individuo_modelo
        # Longitud del tamano genetico del cromosoma
        self.genes = len(individuo_modelo)
        # Cantidad de individuos que se selecciona para la mutacion
        self.poblacion_inicial = poblacion_inicial
        # Poblacion general
        self.poblacion = self.generar_poblacion()
        # Mejor individuo por generacion
        self.mejor_individuo = []
        # Resultado de la funcion fitness para cada individuo de la poblacion
        self.resultado_fitness = []
        # Individuos por generacion con los que se trabajara
        self.constante_por_generacion = constante_por_generacion
        # Individuos que ya estan emparejados
        self.emparejados = []
        # Individuo encontrado
        self.individuo_encontrado = []

    """Crea un individuo aleatorio dentro del rango del numero de genes del individuo modelo."""
    def individual(self, min = 0, max = 1):
            return[random.randint(min, max) for i in range(self.genes)]

    """Genera una poblacion de individuos aleatoria."""
    def generar_poblacion(self):
        return [self.individual() for i in range(self.poblacion_inicial)]

    """Calcula el valor del fitness para cada individuo de la poblacion."""
    def calcular_fitness(self):
        for i in range(len(self.poblacion)):
            res_fitness = 0
            fitness = self.poblacion[i]
            for j in range(len(fitness)):
                res_fitness = res_fitness + abs(self.individuo_modelo[j] - fitness[j])
            self.resultado_fitness.append((-res_fitness, fitness))
            res_fitness = 0
        self.resultado_fitness = sorted(self.resultado_fitness, key=itemgetter(0), reverse=True)
<<<<<<< HEAD
        self.mejor_individuo = self.resultado_fitness[0][1]
        return self.buscar_cero(self.resultado_fitness)


    def buscar_cero( self ,resultado_fitness):
        encontro = False
        print(resultado_fitness)
        for j in range(len(resultado_fitness)):
            if resultado_fitness[j][0] == 0:
                encontro = True
            else:
                self.individuo_encontrado = [j][1]
        return encontro










=======
        self.mejor_individuo = self.resultado_fitness[0][1]
        return True
>>>>>>> 83efe765f05be1265f5c6e6836b50e3acb4e97be


    """De acuardo a la constante_por_generacion de la poblacion general se seleccionan los individuos
    mas cercanos a 0 """
    def seleccionar_poblacion(self):
        self.resultado_fitness = self.resultado_fitness[0:self.constante_por_generacion]

    """Empareja los individuos generados entre si, dejando el individuo con fitness mas alto
    como parte de la siguiente generacion"""
    def emparejar_individuios(self):
        emparejados = []
        restantes = self.resultado_fitness[1:len(self.resultado_fitness)]
        for i in range(len(restantes)):
            emparejados.append((self.mejor_individuo, restantes[i][1]))
        return emparejados

    """Se encarga de mezclar dos individuos, desde una posicion aleatoria."""
    def croosover(self):
        pos = random.randint(1, (len(self.mejor_individuo)-1))
        emparejados = self.emparejar_individuios()
        croosover = []
        for i in range(len(emparejados)):
            croosover.append(emparejados[i][0][0:pos] + emparejados[i][1][pos:len(self.mejor_individuo)])
            croosover.append(emparejados[i][1][0:pos] + emparejados[i][0][pos:len(self.mejor_individuo)])
        return croosover

    """Cambia un bit (0,1) a un numero aleatorio de individuos."""
    def mutacion(self):
        individuos = self.croosover()
        mutaciones = random.randint(0, len(individuos))
        for i in range(mutaciones):
            pos = random.randint(0, len(individuos))
            if individuos[i] == 0:
                individuos[i] = 1
            elif individuos[i] == 1:
                individuos[i] = 0
        return individuos

    """Conforma la poblacion para una siguiente generacion si esta existe,
    tomando los individuos mutados y el mejor individuo de la generacion actual."""
    def poblacion_siguiente_generacion(self):
        del self.poblacion[:]
        mutacion = self.mutacion()
        for i in range(len(mutacion)):
            self.poblacion.append(mutacion[i])
        self.poblacion.append(self.mejor_individuo)
        return(self.poblacion)

    """"""
    def train(self):
        generaciones = 0
        while(self.calcular_fitness()):
            self.seleccionar_poblacion()
            self.emparejar_individuios()
            self.croosover()
            self.poblacion_siguiente_generacion()
            generaciones = generaciones + 1
        print("""Entrenamiento terminado:\n
        Numero de generaciones: {},\n
        Individuo modelo: {},\n
        Individuo encontrado: {},\n""").format(generaciones, self.individuo_modelo, self.individuo_encontrado)
