import random
import sys

inf = 999999

cantPersonas = int(sys.argv[1])
cantProyectos = int(sys.argv[2])

minHoras = []
ofertas = []
demandas = []
resultados = []


### generación de valores

for i in range(cantProyectos):
    rand = round(random.randint(40, 400))
    demandas.append(rand)

for i in range(cantPersonas):
    ofertas.append(160)

for i in range(cantPersonas):
    minHoras.append([])
    resultados.append([])
    for j in range(cantProyectos):
        # Se agregan valores aleatorios
        # Para respetar el intervalo [8,32]
        rand = round(random.randint(40, 160))
        minHoras[i].append(rand)
        resultados[i].append(0)
minHorasCopia = [row[:] for row in minHoras]

### programa principal

def mostrar_matriz(matriz,l):
    for i in range(l):
        print(matriz[i])


def minimo(matriz):
    min = 1000000
    i_min = 0
    j_min = 0
    for i in range(cantPersonas):
        for j in range(cantProyectos):
            if matriz[i][j] < min:
                min = matriz[i][j]
                i_min = i
                j_min = j
    return [i_min,j_min]


def iteracion(ofertas,demandas,i_min,j_min):
    if ofertas[i_min] < demandas[j_min]:
        resultados[i_min][j_min] = ofertas[i_min]
        demandas[j_min] = demandas[j_min] - ofertas[i_min]
        ofertas[i_min] = 0
        for i in range(cantProyectos):
            minHoras[i_min][i] = inf
    elif ofertas[i_min] >= demandas[j_min]:
        resultados[i_min][j_min] = demandas[j_min]
        ofertas[i_min] = ofertas[i_min] - demandas[j_min]
        demandas[j_min] = 0
        for i in range(cantPersonas):
            minHoras[i][j_min] = inf


def iterar():
    i_min, j_min = minimo(minHoras)
    iteracion(ofertas,demandas,i_min,j_min)
    flag = 0
    for i in demandas:
        flag+=i
    if flag != 0:
        iterar()
    else:
        return 0

iterar()

suma = 0

for i in range(cantPersonas):
    for j in range(cantProyectos):
        suma += resultados[i][j]

print(suma)