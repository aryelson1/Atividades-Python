#matriz = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]

#Criando a primeira Matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(4):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz.append(linha)

#Somando os elementos das colunas
somas = []
for i in range(4):
    linha = []
    for j in range(3):
        linha.append(matriz[j][i])
    somas.append(sum(linha))

#Imprimindo Matriz
print(somas)


    