from random import randint
import numpy as np 
from scipy.stats import norm

MAXHT=160

# N personas
# M proyectos

personas = 20
proyectos = 10


presupuesto = []
minHorasProyecto = []

# Matriz NxM 
costosHora = []


# Distribuciones normales para valores aleatorios

X_presupuesto = norm(1200,400)
X_persona = norm(1.5,0.5)
X_minHoras = norm(600,65)

for i in range(personas):
    costosHora.append([])
    for j in range(proyectos):

        # Se agregan valores aleatorios
        # Para respetar el intervalo [1,3]
        rand = round(X_persona.rvs(),2)
        if rand < 1:
            costosHora[i].append(1)
        elif rand > 3:
            costosHora[i].append(3)
        else:
            costosHora[i].append(rand)
    print(costosHora[i])
    

for i in range(proyectos):
    rand = round(X_presupuesto.rvs(),2)

    # Para respetar el intervalo [140,2400]
    if rand < 140:
        presupuesto.append(140)
    elif rand > 2400:
        presupuesto.append(2400)
    else:
        presupuesto.append(rand)


print(presupuesto)

for i in range(proyectos):
    rand = round(X_minHoras.rvs())

    # Para respetar el intervalo [400,800]

    if rand < 400:
        minHorasProyecto.append(400)
    elif rand > 800:
        minHorasProyecto.append(800)
    else:
        minHorasProyecto.append(rand)

#Restriccion min horas
'''for j in range(Proyectos):
    for i in range(Personas):
        print("CH_"+str(i)+"_"+str(j)+" + ")
    print("0 <= "+str(minHorasProyecto[j]))
    print("\n")
'''        
    
#Restriccion max i  
'''for j in range(Proyectos):
    for i in range(Personas):
        print("CH_"+str(i)+"_"+str(j)+" + ")
    print("0 <= "+str(160))
    print("\n")
'''