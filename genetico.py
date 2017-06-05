from operator import itemgetter, attrgetter
import random
import time
import tools as t

class Algoritmo_genetico(object):
    """docstring for Algoritmo_genetico."""
    def __init__(self, individuo_modelo, poblacion_inicial, constante_por_generacion):
        # Modelo de cromosoma, es decir el objetivo que se pretende alcanzar con el algoritmo.
        self.individuo_modelo = individuo_modelo
        # Tamano genetico del cromosoma
        self.genes = len(self.individuo_modelo)
        # Individuos por generacion con los que se trabajara
        self.constante_por_generacion = constante_por_generacion
        # Cantidad de individuos que se selecciona para la mutacion
        self.poblacion = self.generar_poblacion(poblacion_inicial)
        # Mejor individuo por generacion
        self.mejor_individuo = []
        # Numero de generaciones para encontrar el individuo modelo
        self.generaciones = 0

    """Crea un individuo aleatorio dentro del rango del numero de genes del individuo modelo."""
    def individual(self, min = 0, max = 1):
        return [random.randint(min, max) for i in range(self.genes)]

    """Genera una poblacion de individuos aleatoria."""
    def generar_poblacion(self, poblacion_inicial):
        return [self.individual() for i in range(poblacion_inicial)]

    """Calcula el valor del fitness para cada individuo de la poblacion."""
    def fitness(self):
        aux = []
        for i in range(len(self.poblacion)):
            res_fitness = 0
            fitness = self.poblacion[i]
            for j in range(len(fitness)):
                res_fitness = res_fitness + abs(self.individuo_modelo[j] - fitness[j])
            aux.append((-res_fitness, fitness))
        self.poblacion = sorted(aux, key=itemgetter(0), reverse=True)
        self.mejor_individuo = self.poblacion[0][1]
        return self.buscar_cero()

    """Busca dentro de los resultados de la funcion fitness si existe un cero."""
    def buscar_cero(self):
        encontrado = False
        if self.poblacion[0][0] == 0:
            encontrado = True
            self.mejor_individuo = self.poblacion[0][1]
        return encontrado

    """De acueardo a la constante_por_generacion de
    la poblacion general se seleccionan los individuos mas cercanos a 0."""
    def seleccionar_poblacion(self):
        self.poblacion = self.poblacion[0:self.constante_por_generacion]
        self.poblacion = [self.poblacion[i][1] for i in range(len(self.poblacion))]
        return self.poblacion

    """Empareja los individuos generados entre si,
    dejando el individuo con fitness mas alto como parte de
    la siguiente generacion"""
    def emparejar(self):
        aux = []
        restantes = self.poblacion[1:len(self.poblacion)]
        for i in range(len(restantes)):
            aux.append((self.mejor_individuo, restantes[i]))
        self.poblacion = aux
        return self.poblacion

    """Se encarga de mezclar dos individuos, desde una posicion aleatoria."""
    def croosover(self):
        cross = []
        for i in range(len(self.poblacion)):
            pos = random.randint(1, (len(self.mejor_individuo)-1))
            cross.append(self.poblacion[i][0][0:pos] + self.poblacion[i][1][pos:len(self.mejor_individuo)])
            cross.append(self.poblacion[i][1][0:pos] + self.poblacion[i][0][pos:len(self.mejor_individuo)])
        self.poblacion = cross
        return self.poblacion

    """Cambia un bit (0,1) a un numero aleatorio de individuos."""
    def mutacion(self):
        for i in range(random.randint(0,len(self.poblacion)-1)):# Revisar -1
            pos = random.randint(0, len(self.poblacion[i])-1)# Revisar -1
            if self.poblacion[i][pos] == 0:
                self.poblacion[i][pos] = 1
            elif self.poblacion[i][pos] == 1:
                self.poblacion[i][pos] = 0
        return self.poblacion

    """Conforma la poblacion para una siguiente generacion si esta existe,
    tomando los individuos mutados y el mejor individuo de la generacion actual."""
    def siguiente_generacion(self):
        generacion = []
        generacion.append(self.mejor_individuo)
        for i in range(len(self.poblacion)):
            generacion.append(self.poblacion[i])
        self.poblacion = generacion[0:self.constante_por_generacion]
        return self.poblacion

    """Itera hasta encontrar el individuo modelo."""
    def train(self):
        while not self.fitness():
            self.seleccionar_poblacion()
            self.emparejar()
            self.croosover()
            self.mutacion()
            self.siguiente_generacion()
            self.generaciones = self.generaciones + 1
        print("""Entrenamiento terminado:\n
        Numero de generaciones: {},\n
        Individuo modelo: {},\n
        Individuo encontrado: {},\n""").format(self.generaciones, self.individuo_modelo, self.mejor_individuo)

    """Regresa todos los parametros de la clase."""
    def to_string(self):
        return "Individuo modelo: {}\nNumero de genes: {}\nPoblacion: {}\nConstante por generacion: {}\n".format(self.individuo_modelo, self.genes, len(self.poblacion), self.constante_por_generacion)
