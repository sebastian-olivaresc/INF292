#! /usr/bin/env python


import random 
import numpy as np
from datetime import datetime

random.seed(datetime.now().timestamp())

class instancia:
    def __init__(self, M, L, default):
        self.D = default*random.randint(1, L) # demanda en mes i 
        self.C = default*random.randint(1, L) # precio produccion normal 
        self.K = default*random.randint(1, L) # precio produccion extra
        self.A = random.randint(1000,2000) # capacidad max almacen
        self.P = random.randint(1, L) # precio unitario mensual almacen
        self.N = random.randint(1, L) # produccion max normal

def crear_instancia(M):
    L = 100 # fija el limite de la variacion de costos y demandas
    default = np.arange(1, M)
    return instancia(M, L, default)

def printear_instancia(inst):
    print("D_i: ", inst.D)
    print("C_i: ", inst.C)
    print("K_i: ", inst.K)
    print("A: ", inst.A)
    print("P: ", inst.P)
    print("N: ", inst.N)

M_p =[[5, 10], [10, 20], [20, 30], [30, 40], [40, 50]]
M_m =[[100, 130], [130, 160], [160, 180], [170, 190], [190, 200]]
M_g =[[400, 600], [500, 700], [600, 800], [700, 900], [800, 1000]]

rangos_M = [M_p, M_m, M_g]

instancias = list()
for lista in rangos_M:
    for limites in lista:
        bot, top = limites
        M = random.randint(bot, top)
        instancias.append(crear_instancia(M))

for i in range(len(instancias)):
    print("-"*10)
    print("Instancia ", i+1,)
    printear_instancia(instancias[i])
    print("-"*10)
print("-"*10)
