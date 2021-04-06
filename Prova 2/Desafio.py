primo = 1
soma = 0
n1 = int(input())
n2 = int(input())

while n2 <= n1:
    print("Digite um valor maior que o primeiro!")
    n2 = int(input())
    
for i in range(n1,n2+1):
    if i > 3:
        for count in range(2,n1):
            if (i % count == 0):
                primo = 0
                break
        if i % 2 == 0:
            primo = 0
    if primo == 1:
        soma += i
    primo = 1

if soma > 0:
    print(soma)
else:
    print("Sem n�meros primos no intervalo informado.")