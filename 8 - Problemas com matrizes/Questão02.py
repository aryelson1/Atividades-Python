
#matriz = [[1,3,7],[4,-2,0]]
#matriz2 = [[10,20,-7],[5,14,3]]


#Criando a primeira Matriz
matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz.append(linha)

#Criando a segunda Matriz
matriz2 = []
for i in range(2):
    linha = []
    for j in range(3):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz2.append(linha)

#Somando as duas matrizes
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[0])):
        linha.append(matriz[i][j] + matriz2[i][j])
    print(linha)

