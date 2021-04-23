matriz = []
n = int(input())

for i in range(n):
    linha = input().split()
    linha = list(map(int,linha))
    matriz.append(linha)

matriz2 = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(matriz[j][i])
    matriz2.append(linha)

for i in range(n):
    for j in range(n):
        if matriz2[i][j] < 0:
            matriz2[i][j] *= 2

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(matriz2[i][j])
        else:
            print(matriz2[i][j], end = ' ')