n = int(input())
lista = input().split()
lista = list(map(int,lista))

num = lista[0]
cont = 1
lista2 = []
for i in range(1,n):
  if num == lista[i]:
    cont += 1
  else:
    lista2.append(cont)
    num = lista[i]
    cont = 1
    
lista2.append(cont)
print(max(lista2))

    
