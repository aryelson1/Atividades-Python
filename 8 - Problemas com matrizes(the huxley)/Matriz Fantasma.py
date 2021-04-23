matriz = []
n = int(input())
for i in range(n):
    linha = []
    for j in range(1,n+1):
        linha.append(j)
    matriz.append(linha)
    
for i in range(1,n):
    for j in range(0,i):
        matriz[i][j] = " "
            

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(matriz[i][j])
        else:
            print(matriz[i][j], end = ' ')