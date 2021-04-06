#variaveis
m=0
n= 0
#entrada
n = int(input())
m = int(input())
#Processamento
for i in range(n,m+1):
    if i % 2 != 0:
        print(i)
