from genetico import Algoritmo_genetico

if __name__ == '__main__':

    individuo_modelo = [1,1,0,1,0,0,1,0]

    poblacion_inicial = 5

    constante_por_generacion = 4

    genetico = Algoritmo_genetico(individuo_modelo, poblacion_inicial, constante_por_generacion)
    
    genetico.train()
