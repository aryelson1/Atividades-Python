ci = 0
ca = 0
h = 0
m = 0

while True:
    nota1 = int(input())
    if nota1 < 0:
        break
    while nota1 > 100:
        print("Digite uma nota inferior a 100.")
        nota1 = int(input())
    nota2 = int(input())
    while nota2 > 100:
        print("Digite uma nota inferior a 100.")
        nota2 = int(input())
    sexo = input().upper()
    ci += 1
    if nota1 > 40 and nota2 > 40 and (nota1+nota2)/2 >= 60:
        ca += 1
        if sexo == "M":
            h += 1 
        elif sexo == "F":
            m += 1

print("%d candidato(s) inscrito(s)."%ci)
print("%d candidato(s) aprovado(s)."%ca)
print("%d mulher(es) e %d homem(ns)."%(m,h))