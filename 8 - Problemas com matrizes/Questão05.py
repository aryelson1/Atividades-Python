import numpy as np

'''
matriz = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
print(np.transpose(matriz))
'''
#Criando a primeira Matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(4):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz.append(linha)

#Fazendo a transposta da matriz(linha vira coluna )
matriz2 = []
for i in range(4):
    linha = []
    for j in range(3):
        linha.append(matriz[j][i])
    matriz2.append(linha)

#Imprimindo Matriz
for i in matriz2:
    print(i)

