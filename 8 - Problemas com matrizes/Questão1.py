matriz = [[1,2,3],[8,10,12],[21,24,27]]
lin = int(input())
col = int(input())
'''
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input()))
    matriz.append(linha)
'''
if lin == 0:
    if col == 0:
        soma = matriz[lin][col]+matriz[lin][col+1]+matriz[lin+1][col]
    elif col == len(matriz[0]):
        soma = matriz[lin][col]+matriz[lin][col-1]+matriz[lin+1][col]
    else:
        soma = matriz[lin][col]+matriz[lin][col-1]+matriz[lin][col+1]+matriz[lin+1][col]
elif lin == len(matriz) - 1 :
    if col == 0:
        soma = matriz[lin][col]+matriz[lin][col+1]+matriz[lin-1][col]
    elif col == len(matriz[0])-1:
        soma = matriz[lin][col]+matriz[lin][col-1]+matriz[lin-1][col]
    else:
        soma = matriz[lin][col]+matriz[lin][col-1]+matriz[lin][col+1]+matriz[lin-1][col]
elif col == 0:
    soma = matriz[lin][col]+matriz[lin][col+1]+matriz[lin+1][col]+matriz[lin-1][col]
elif col == len(matriz[0]) - 1:
    soma = matriz[lin][col]+matriz[lin][col-1]+matriz[lin+1][col]+matriz[lin-1][col]
else:
    soma = matriz[lin][col] + matriz[lin][col+1] + matriz[lin][col-1] + matriz[lin-1][col] + matriz[lin+1][col]

print(soma)