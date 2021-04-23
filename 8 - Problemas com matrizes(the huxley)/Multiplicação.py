while True:
    n = int(input())
    if n == 0:
        break
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(int(input()))
        matriz.append(linha)
    matriz2 = []
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(matriz[j][i])
        matriz2.append(linha)
        
    for i in range(4):
        matriz2[i][i] *= n
    
    for i in matriz2:
        for j in i:
            print(j, end = ' ')
        print()