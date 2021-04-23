matriz = []
menor = 0

dms = input().split()
li = int(dms[0])
col = int(dms[1])

for i in range(li):
    linha = []
    for j in range(col):
        n = int(input())
        if n < 0:
            menor += 1 
        linha.append(n)
    matriz.append(linha)
print("Matriz formada:")

for i in range(li):
    for j in range(col):
        if j == col-1:
            print(matriz[i][j])
        else:
            print(matriz[i][j], end = ' ')
    

if li != col:
    print("A diagonal principal e secundaria nao pode ser obtida.")
else:
    dp = 0
    ds = 0
    for i in range(li):
        dp += matriz[i][i]
    matriz.reverse()
    for i in range(li):
        ds += matriz[i][i]
    print("A diagonal principal e secundaria tem valor(es) %i e %i respectivamente."%(dp,ds))

print("A matriz possui %i numero(s) menor(es) que zero."%menor)
print("A matriz possui %i numero(s) maior(es) que zero."%((li*col)-menor))