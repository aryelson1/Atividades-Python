n1 = int(input())
n2 = int(input())
n3 = int(input())
maior = 0
menor = 0
meio = 0

if n1 > n2 and n1 > n3 and n2 > n3:
    meio = n2
elif n2 > n1 and n2 > n3 and n1 > n3:
    meio = n1
elif n3 > n1 and n3 > n2 and n1 > n2:
    meio = n1
elif n3 > n1 and n3 > n2 and n2 > n1:
    meio = n2
elif n2 > n1 and n2 > n3 and n3 > n1:
    meio = n3
elif n1 > n2 and n1 > n3 and n3 > n2:
    meio = n3

print(meio)