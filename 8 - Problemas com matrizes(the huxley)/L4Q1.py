li = int(input())
col = int(input())
matriz = []
for i in range(li):
    linha = []
    for j in range(col):
        linha.append(int(input()))
    matriz.append(linha)
    
if li == col:
    somaP = 0
    somaS = 0
    for i in range(li):
        somaP += matriz[i][i] 
    matriz.reverse()
    for i in range(li):
        somaS += matriz[i][i]
    print(somaP)
    print(somaS)
    matriz.reverse()
else:
    print("A matriz nao possui traco")


for i in range(li):
    for j in range(col):
        if j == col-1:
            print(matriz[i][j])
        else:
            print(matriz[i][j], end = ' ')