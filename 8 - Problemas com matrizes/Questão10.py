matriz = [['O', 'X', 'O'],['X', 'O', 'X'],['X', 'X', 'O'] ]
#matriz =  [['O', 'X', 'X'],['X', 'X', 'O'],['O', 'O', 'X'] ]

'''
#Criando a primeira Matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(input("linha %i e Coluna %i: "%(i,j)))
    matriz.append(linha)

#Criando a segunda Matriz
matriz2 = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(input("linha %i e Coluna %i: "%(i,j)))
    matriz2.append(linha)
'''


#Verificando os elementos das colunas
verf = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz[j][i])
    verf.append(linha)

#Verificando os elementos das linhas
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz[i][j])
    verf.append(linha)

#Verificando os elementos da diagonal PRINCIPAL
linha = []
for i in range(3):
    linha.append(matriz[i][i])
verf.append(linha)

#Verificando os elementos da diagonal SECUNDARIA
linha = []
matriz.reverse()
for i in range(3):
    linha.append(matriz[i][i])
verf.append(linha)

ganhou = 2
for i in verf:
    if i.count("O") == 3:
        ganhou = 0
    elif  i.count("X") == 3:
        ganhou = 1

if ganhou == 0:
    print("O ganhou")
elif ganhou == 1:
    print("X ganhou")
else:
    print("Ninguem ganhou")