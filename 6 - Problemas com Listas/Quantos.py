n = int(input())
lista2 = []
for i in range(n):
    n1=int(input())
    lista2.append(n1)
x = sum(lista2) / n
maior =x*1.10
menor =x*0.90
n2 = 0
n3 = 0
for n in lista2:
    if n >= maior:
        n2+=1
    elif n <= menor:
        n3+=1
print("%.2f"% x)
print(n2)
print(n3)