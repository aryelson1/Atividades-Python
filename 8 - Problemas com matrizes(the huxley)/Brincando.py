matriz = []
cont = 0
media = 0
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input()))
    matriz.append(linha)

for i in matriz:
    for j in i:
        if j > 0:
            media += j
            cont += 1
media = media / cont

minimo = matriz[0][0]
for i in matriz:
   if minimo > min(i):
     minimo = min(i)
     

if minimo % 2 == 0:
    delta = 1
else:   
    delta = 0
    
for i in range(3):
    matriz[i][i] = 0
    
soma = 0
for i in matriz:
    soma += sum(i)

print("%.2f %d %d %d"%(media,minimo,delta,soma))


