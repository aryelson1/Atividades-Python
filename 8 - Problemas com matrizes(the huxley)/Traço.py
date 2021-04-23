n = int(input())

matriz = []
for i in range(n):
    linha = input().split()
    linha = list(map(float,linha))
    matriz.append(linha)

soma = 0
for i in range(n):
    soma += matriz[i][i] 

print("tr(A) = ",end="")
for i in range(n):
    if i == n-1:
        print("(%.2f) = %.2f"%(matriz[i][i],soma))
    else:
        print("(%.2f) + "%matriz[i][i],end="")