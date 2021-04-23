matriz = []
dms = input().split()
li = int(dms[0])
col = int(dms[1])

for i in range(li):
    linha = input().split()
    linha = list(map(int,linha))
    matriz.append(linha)



matriz2 = []
for i in range(col):
    linha = []
    for j in range(li):
        linha.append(matriz[j][i])
    matriz2.append(linha)

for i in range(col):
    for j in range(li):
        print(matriz2[i][j], end = ' ')
    print()