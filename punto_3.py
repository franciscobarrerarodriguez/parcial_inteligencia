from genetico import Algoritmo_genetico

if __name__ == '__main__':

    poblacion_inicial = 5

    constante_por_generacion = 4

    individuos = [
     [0,1,0,0,1,0,0,0],# H
     [0,1,0,0,1,1,1,1],# O
     [0,1,0,0,1,1,0,0],# L
     [0,1,0,0,0,0,0,1],# A
     [0,1,0,0,1,1,0,1],# M
     [0,1,0,1,0,1,0,1],# U
     [0,1,0,0,1,1,1,0],# N
     [0,1,0,0,0,1,0,0],# D
     [0,1,0,0,1,1,1,1]# O
    ]

    for i in range(len(individuos)):
        genetico = Algoritmo_genetico(individuos[i], poblacion_inicial, constante_por_generacion)
        genetico.train()
