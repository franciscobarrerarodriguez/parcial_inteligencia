
import random
from builtins import print

import  numpy as np
cromosoma=np.array([1, 1, 0, 1, 0, 0, 1, 0])
gen= 8
num = 5
cantidad = 10
mutacion = 0.2
individuos=4

def individual(min, max):
    return[random.randint(min, max) for i in range(gen)]

def crearPoblacion():
    return [individual(0,1) for i in range(num)]

def calcularFitness():
    poblacion = crearPoblacion()
    for i in range(len(poblacion)):
        res = 0
        objetivo = poblacion[i]
        for j in range(len(objetivo)):
            res = res + abs(objetivo[j]-cromosoma[j])
        print(-res)
        res = 0
print(cromosoma)
print(crearPoblacion())
calcularFitness()

