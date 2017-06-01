from operator import itemgetter, attrgetter
import random
import  numpy as np

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
        # Resultado de la funcion fitness para cada individuo de la poblacion
        self.resultado_fitness = []
        # Individuos por generacion con los que se trabajara
        self.constante_por_generacion = constante_por_generacion
        # Individuos que ya estan emparejados
        self.emparejados = []

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

    """De acuardo a la constante_por_generacion de la poblacion general se seleccionan los individuos
    mas cercanos a 0 """
    def seleccionar_poblacion(self):
        self.resultado_fitness = self.resultado_fitness[0:self.constante_por_generacion]

    """Empareja los individuos generados entre si, dejando el individuo con fitness mas alto
    como parte de la siguiente generacion"""
    def emparejar_individuios(self):
        emparejados = []
        mejor_individuo = self.resultado_fitness[0][1]
        restantes = self.resultado_fitness[1:len(self.resultado_fitness)]
        for i in range(len(restantes)):
            emparejados.append((mejor_individuo, restantes[i][1]))
        print(mejor_individuo)
        return emparejados

        # print(restantes)
        # print("\n")
        # print(emparejados)
        # emparejados = []
        # for i in range(len(individuos)):
        #     emparejados.append(mejor_individuo, individuos[i])
        # print(emparejados)


if __name__ == "__main__":

    individuo_modelo = np.array([1, 1, 0, 1, 0, 0, 1, 0])
    poblacion_inicial = 10
    constante_por_generacion = 8

    genetico = Algoritmo_genetico(individuo_modelo, poblacion_inicial, constante_por_generacion);

    print("Individuo_modelo: {}, numero de genes: {} \n").format(genetico.individuo_modelo, genetico.genes)
    print("Prueba individual: {} ").format(genetico.individual())
    print("Poblacion:\n")
    print("{} \n").format(genetico.poblacion)
    print("Resultado de fitness:\n")
    genetico.calcular_fitness()
    print("{} \n").format(genetico.resultado_fitness)
    print("Individuos seleccionados:\n")
    genetico.seleccionar_poblacion()
    print("{} \n").format(genetico.resultado_fitness)
    print("Emparejados:\n")
    print(genetico.emparejar_individuios())
