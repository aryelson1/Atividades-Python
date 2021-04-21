#matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#matriz2 = [[10, 11, 12],[13, 14, 15],[ 7, 8, 9]]


#Criando a primeira Matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz.append(linha)

#Criando a segunda Matriz
matriz2 = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz2.append(linha)

#Verificando se são elementos iguais na mesma posição(linha e coluna)
matriz3 = []
for i in range(3):
    linha = []
    for j in range(3):
        if matriz[i][j] == matriz2[i][j]:
            linha.append(matriz[i][j])
        else:
            linha.append(0)
    matriz3.append(linha)

#Imprimindo Matriz
for i in matriz3:
    print(i)


