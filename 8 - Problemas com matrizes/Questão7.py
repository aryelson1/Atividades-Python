#matriz = [[4,0,0],[0,2,0],[1,0,1]]
#matriz = [[4,3, 1],[0,2,1],[0,0,1]]


#Criando a primeira Matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("linha %i e Coluna %i: "%(i,j))))
    matriz.append(linha)
    
'''
#Verificando se é triangular Inferior
Triangular = True
for i in range(3): # 3 é o numero de linhas da matriz
    for j in range(i+1,3): # é o numero de colunas da matriz
        if matriz[i][j] != 0:
            Triangular = False
'''

#Verificando se é triangular Superior
Triangular = True
for i in range(1,3):
    for j in range(0,i):
        if matriz[i][j] != 0:
            Triangular = False

if Triangular:
    print("É uma matriz triangular superior.")
else:
    print("Não é uma matriz triangular superior.")