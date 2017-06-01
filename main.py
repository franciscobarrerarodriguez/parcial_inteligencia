from genetico import Algoritmo_genetico

import  numpy as np

if __name__ == "__main__":

    individuo_modelo = np.array([1, 1, 0, 1, 0, 0, 1, 0])
    poblacion_inicial = 5
    constante_por_generacion = 4

    genetico = Algoritmo_genetico(individuo_modelo, poblacion_inicial, constante_por_generacion );

    #genetico.train()

    print(genetico.calcular_fitness())




    # print("Individuo_modelo: {}, numero de genes: {} \n").format(genetico.individuo_modelo, genetico.genes)

    # print("Prueba individual: {} ").format(genetico.individual())

    # print("Poblacion:\n")
    # print("{} \n").format(genetico.poblacion)
    # print("Resultado de fitness:\n")
    # genetico.calcular_fitness()
    # print("{} \n").format(genetico.resultado_fitness)
    # print("Individuos seleccionados:\n")
    # genetico.seleccionar_poblacion()
    # print("{} \n").format(genetico.resultado_fitness)
    # print("Mejor individuo: {}\n").format(genetico.mejor_individuo)
    # print("Emparejados:\n")
    # print(genetico.emparejar_individuios())
    # print("Croosover:\n")
    # print(genetico.croosover())
    # print("\nMutacion:\n")
    # genetico.mutacion()
    # print("\nSiguiente generacion:\n")
    # genetico.poblacion_siguiente_generacion()


