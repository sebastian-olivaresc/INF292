#! /usr/bin/env python

import random 
import numpy as np
import math
from datetime import datetime

random.seed(datetime.now().timestamp())

# clase que contiene los datos de una instancia
class instancia:
    def __init__(self, M, L, demanda_alta, default):
        self.C = default*random.randint(1, L) # precio produccion normal 
        self.K = default*random.randint(1, L) # precio produccion extra
        self.P = random.randint(1, L) # precio unitario mensual almacen

        self.A = random.randint(1000,2000) # capacidad max almacen
        self.N = random.randint(1, L) # produccion max normal
        
        # restriccion de la demanda maxima
        rest = math.ceil(((3/2) * self.N + self.A) / default[M-2])

        if (demanda_alta == True):
            base_demanda = random.randint(math.ceil(rest/2), rest)
        else:
            base_demanda = random.randint(1, math.ceil(rest/2))

        self.D = default*base_demanda

def crear_instancia(M):
    L = 1000 # fija el limite de la variacion de costos y demandas
    escala = random.randint(1, 100)
    default = np.arange(1+escala, M+escala)
    tipo_demanda = bool(random.getrandbits(1)) 
    return instancia(M, L, tipo_demanda, default)

def stringify_instancias(inst):
    a = "D_i: "+str(inst.D)+"\n"+ \
    "C_i: "+str(inst.C)+"\n"+ \
    "K_i: "+str(inst.K)+"\n"+\
    "A: "+str(inst.A)+"\n"+\
    "P: "+str(inst.P)+"\n"+\
    "N: "+str(inst.N)+"\n"

    return a

M_p =[[5, 10], [10, 20], [20, 30], [30, 40], [40, 50]]
M_m =[[100, 130], [130, 160], [160, 180], [170, 190], [190, 200]]
M_g =[[400, 600], [500, 700], [600, 800], [700, 900], [800, 1000]]

rangos_M = [M_p, M_m, M_g]

f = open("instancias.txt", "w")

instancias = list()
for lista in rangos_M:
    for limites in lista:
        bot, top = limites
        M = random.randint(bot, top)
        instancias.append(crear_instancia(M))

for i in range(len(instancias)):
    f.write("-"*10+"\n")
    f.write("Instancia "+str(i+1)+"\n")
    f.write(stringify_instancias(instancias[i]))
    f.write("-"*10+"\n")
f.write("-"*10+"\n")

f.close()
