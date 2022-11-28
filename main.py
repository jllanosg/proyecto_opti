from random import randint
import numpy as np 
from scipy.stats import norm

# N cantPersonas
# M cantProyectos

cantPersonas = 5
cantProyectos = 6

# Listas de largo M
presupuesto = []
minHorasProyectoTotal = []

# Matriz NxM 
costosHora = []
minHoras = []

# Distribuciones normales para valores aleatorios

X_presupuesto = norm(1200,400)
X_persona = norm(1.5,0.5)
X_minHoras = norm(600,65)

# minimo de horas en un proyecto
X_minHorasNM = norm(20,4)

#####################################
### GENERACION VALORES ALEATORIOS ###
#####################################


for i in range(cantPersonas):
    costosHora.append([])
    for j in range(cantProyectos):

        # Se agregan valores aleatorios
        # Para respetar el intervalo [1,3]
        rand = round(X_persona.rvs(),2)
        if rand < 1:
            costosHora[i].append(1)
        elif rand > 3:
            costosHora[i].append(3)
        else:
            costosHora[i].append(rand)
    

for i in range(cantProyectos):
    rand = round(X_presupuesto.rvs(),2)

    # Para respetar el intervalo [140,2400]
    if rand < 140:
        presupuesto.append(140)
    elif rand > 2400:
        presupuesto.append(2400)
    else:
        presupuesto.append(rand)


#print(presupuesto)

for i in range(cantProyectos):
    rand = round(X_minHoras.rvs(),2)

    # Para respetar el intervalo [400,800]

    if rand < 400:
        minHorasProyectoTotal.append(400)
    elif rand > 800:
        minHorasProyectoTotal.append(800)
    else:
        minHorasProyectoTotal.append(rand)

for i in range(cantPersonas):
    minHoras.append([])
    for j in range(cantProyectos):
        # Se agregan valores aleatorios
        # Para respetar el intervalo [8,32]
        rand = round(X_minHorasNM.rvs(),2)
        if rand < 8:
            minHoras[i].append(8)
        elif rand > 32:
            minHoras[i].append(32)
        else:
            minHoras[i].append(rand)
    print(minHoras[i])


#######################################
### GENERACION STRINGS RESTRICIONES ###
#######################################


# Restricción presupuesto
# Restricción máx de empleados por cantProyectos
# Restricción min de horas del proyecto

restPresupuesto = []  # Ejemplo: ['C_0_0 + C_1_0 + C_2_0 + C_3_0 + C_4_0 <= 1760.98', 'C_0_1 + C_1_1 + C_2_1 + C_3_1 + C_4_1 <= 1456.1']
restMaxEmpleados = [] # Ejemplo: ['X_0_0 + X_1_0 + X_2_0 + X_3_0 + X_4_0 <= 5', 'X_0_1 + X_1_1 + X_2_1 + X_3_1 + X_4_1 <= 5']
restMinHoras = [] # Ejemplo: ['H_0_0 + H_0_1 + H_0_2 + H_0_3 + H_0_4 >=701.59;', 'H_1_0 + H_1_1 + H_1_2 + H_1_3 + H_1_4 >=493.55;', ...]


for j in range(cantProyectos):
    string1 = ""
    string2 = ""
    string3 = ""
    for i in range(cantPersonas):
        if i == cantPersonas-1:
            string1 += "C_"+str(j)+"_"+str(i)
            string2 += "X_"+str(j)+"_"+str(i)
            string3 += "H_"+str(j)+"_"+str(i)
        else:
            string1 += "C_"+str(j)+"_"+str(i)+" + "
            string2 += "X_"+str(j)+"_"+str(i)+" + "
            string3 += "H_"+str(j)+"_"+str(i)+" + "
    string1 += " <= "+str(presupuesto[j])+";"
    string2 += " <= 5;"
    string3 += " >= "+ str(minHorasProyectoTotal[j]) +";"
    restPresupuesto.append(string1)
    restMaxEmpleados.append(string2)
    restMinHoras.append(string3)


# Restricción máx cantProyectos por persona
# Restricción máx horas por persona

restMaxProyectos = [] # Ejemplo: ['X_0_0 + X_0_1 + X_0_2 + X_0_3 + X_0_4 + X_0_5<= 5', 'X_1_0 + X_1_1 + X_1_2 + X_1_3 + X_1_4 + X_1_5<= 5', ...]
restMaxHoras = []
restMinHoras = []

for i in range(cantPersonas):
    string = ""
    string2 = ""
    for j in range(cantProyectos):
        if j == cantProyectos-1:
            string += "X_"+str(j)+"_"+str(i)
            string2 += "H_"+str(j)+"_"+str(i)
        else:
            string += "X_"+str(j)+"_"+str(i)+" + "
            string2 += "H_"+str(j)+"_"+str(i)+" + "
    string += " <= 5;"
    string2 += " <= 160;"
    restMaxProyectos.append(string)
    restMaxHoras.append(string2)

for i in range(cantPersonas):
    restMinHoras.append([])
    for j in range(cantProyectos):
            restMinHoras[i].append("H_"+str(j)+"_"+str(i)+">="+str(minHoras[i][j])+";")
    print(restMinHoras[i])

