n = int(input())
lista = input().split()
lista = list(map(int,lista))
cont = 1
maior = 0
for i in range(n-1):
    if lista[i] == lista[i+1]:
        cont += 1
    else:
        cont = 1
    if cont > maior:
        maior = cont
print(maior)
