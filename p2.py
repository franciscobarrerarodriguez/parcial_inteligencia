from genetico import Algoritmo_genetico
import tools as t
import time

if __name__ == '__main__':

    poblacion = t.arreglo_binario(255)

    individuo_modelo = [1,1,0,1,0,0,1,0]

    poblacion_inicial = 5

    constante_por_generacion = 4

    genetico = Algoritmo_genetico(individuo_modelo, poblacion_inicial, constante_por_generacion)

    start_time = time.time()

    genetico.iterar_individual(poblacion, individuo_modelo)
    
    print("Tiempo de ejeucion: {} segundos").format(time.time() - start_time)
