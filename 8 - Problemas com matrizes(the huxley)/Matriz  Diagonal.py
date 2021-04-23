matriz = []
n = int(input())
cont = 1
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(cont)
        cont += 1
    matriz.append(linha)
print("Matriz:")
for i in range(n):
    for j in range(n):
        if j == 0:
             print(" ",matriz[i][j], end = '  ')
        else:
            if j == n-1:
                 print(matriz[i][j])
            else:
                print(matriz[i][j], end = '  ')

print()
print("Diagonal Principal:")
for i in range(1,n):
    for j in range(0,i):
        matriz[i][j] = " "
for i in range(n): 
    for j in range(i+1,n): 
       matriz[i][j] = " "
for i in range(n):
    for j in range(n):
        if matriz[i][j] != " ":
            print(" ",matriz[i][j], end = '')
            break
        else:
             print(" ",matriz[i][j], end = '')
    print()
print()
matriz = []
cont = 1
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(cont)
        cont += 1
    matriz.append(linha)  
print("Diagonal Secundaria:")
matriz.reverse()
for i in range(1,n):
    for j in range(0,i):
        matriz[i][j] = " "
for i in range(n): 
    for j in range(i+1,n): 
       matriz[i][j] = " "
matriz.reverse()
for i in range(n):
    for j in range(n):
        if matriz[i][j] != " ":
            print(" ",matriz[i][j], end = '')
            break
        else:
            print(" ",matriz[i][j], end = '')
    print()
