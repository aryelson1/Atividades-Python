
#Criando a matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz.append(linha)


#matriz = [[1,2,3],[8,10,12],[21,24,27]]

#Imprimindo a diagonal
for i in range(3):
    print(matriz[i][i], end = " ")

