from random import randint
MAXHT=160

Personas = 20
Proyectos = 10
presupuesto = []
minhr = []
CH = []

for i in range(Personas):
    CH.append([])
    for j in range(Proyectos):
        CH[i].append(randint(1,3))
    #print(CH[i])

for i in range(Proyectos):
    presupuesto.append(randint(160,2400))
print(presupuesto)

for i in range(Proyectos):
    minhr.append(randint(400,800))
print(minhr)

#Restriccion min horas
'''for j in range(Proyectos):
    for i in range(Personas):
        print("CH_"+str(i)+"_"+str(j)+" + ")
    print("0 <= "+str(minhr[j]))
    print("\n")
'''        
    
#Restriccion max i  
'''for j in range(Proyectos):
    for i in range(Personas):
        print("CH_"+str(i)+"_"+str(j)+" + ")
    print("0 <= "+str(160))
    print("\n")
'''