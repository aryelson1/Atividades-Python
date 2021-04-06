i = int(input())
f = int(input())

if i > f :
    print("Eu odeio a professora!")
elif i <= f-3:
    print("Muito bem! No prazo!")
else :
    print("Parece o trabalho do meu filho!")
    if f+2 <= 24:
        print("Trabalho Apresentado!")
    else:
        print("Voce falhou! Ate a proxima!")