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
        return self.poblacion

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




    def to_string(self):
        return "Individuo modelo: {}\nNumero de genes: {}\nPoblacion: {}\nConstante por generacion: {}\n".format(self.individuo_modelo, self.genes, len(self.poblacion), self.constante_por_generacion)

if __name__ == '__main__':

    individuo_modelo = [1,1,0,1,0,0,1,0]
    poblacion_inicial = 5
    constante_por_generacion = 4
    genetico = Algoritmo_genetico(individuo_modelo, poblacion_inicial, constante_por_generacion)

    print (genetico.to_string())
    # print ("Prueba individual: {}\n").format(genetico.individual())
    print ("Poblacion:\n\n{}").format(t.beautify(genetico.poblacion))

    print("Resultado fitness:\n\n{}").format(t.beautify(genetico.fitness()))

    if(genetico.buscar_cero()):
        print("\nCero encontrado, individuo: {}").format(genetico.mejor_individuo)
    else:
        print("\nCero no encontrado, mejor individuo: {}").format(genetico.mejor_individuo)
        print ("\nPoblacion seleccionada:\n\n{}").format(t.beautify(genetico.seleccionar_poblacion()))
        print("\nPoblacion emparejada:\n\n{}").format(t.beautify(genetico.emparejar()))


    # genetico.poblacion = [
    # (0, [1, 0, 0, 0, 0, 0, 0, 1]),
    # (-3, [1, 1, 0, 1, 0, 0, 1, 0]),
    # (-1, [0, 1, 0, 1, 0, 1, 0, 1]),
    # (-5, [0, 0, 1, 0, 1, 0, 1, 0]),
    # (-6, [1, 1, 1, 0, 1, 1, 0, 1])]
    #
    # print("\nPrueba buscar cero: {}\n{}").format(genetico.buscar_cero(), genetico.mejor_individuo)
