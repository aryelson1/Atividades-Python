matriz = [[1,2,3],[8,10,12],[21,24,27]]

#invertendo a matriz matriz = [[21,24,27],[8,10,12],[1,2,3]]
matriz.reverse()

#Imprimindo a diagonal secundaria
for i in range(2,-1,-1):
    print(matriz[i][i], end = " ")

