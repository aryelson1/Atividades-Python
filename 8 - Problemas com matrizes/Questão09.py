#matriz = [[2,7,6],[9,5,1],[4,3,8]]
#matriz = [[1,2,3],[4,5,6], [9,0,7]]

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

#Somando os elementos das colunas
somas = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz[j][i])
    somas.append(sum(linha))

#Somando os elementos das linhas
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz[i][j])
    somas.append(sum(linha))

#Somando os elementos da diagonal PRINCIPAL
linha = []
for i in range(3):
    linha.append(matriz[i][i])
somas.append(sum(linha))

#Somando os elementos da diagonal SECUNDARIA
linha = []
matriz.reverse()
for i in range(3):
    linha.append(matriz[i][i])
somas.append(sum(linha))

#Verificando se é quadrado mágico
if somas.count(somas[0]) == 8:
    print("É uma matriz de quadrado mágico !")
else:
    print("Não é uma matriz de quadrado mágico !")