n = int(input())
lista = input().split()

lista = list(map(int,lista))
    
lista2 = lista.copy()
lista2.sort()

print("Menor valor:",lista2[0])
print("Posicao:",lista.index(lista2[0]))