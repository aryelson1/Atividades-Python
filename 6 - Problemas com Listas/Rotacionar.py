n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
    
pulo = int(input())

for i in range(n):
    if i + pulo < n:
        print(lista[i+pulo])
    else:
        print(lista[(i+pulo)-n]) 
