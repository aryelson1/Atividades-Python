totalAV = 0
totalC = 0
maior = 0
media = 0
cont = 0
contAV =  0
idade = 100

while True:
    id = int(input())
    valor = float(input())
    tipo = input()
    ct = input()
    if id < idade:
        idade = id
        
    if tipo == "C":
        totalC += valor
    else:
        totalAV += valor
        contAV += 1
    if valor > maior:
        maior = valor
    cont += 1
    if ct == "N":
        break
    
print(cont)
if totalAV == 0:
    print(0)
else:
    print("%.2f"%totalAV)
if totalC == 0:
    print(0)
else:
    print("%.2f"%totalC)
print(idade)
print("%.2f"%maior)
if contAV == 0:
    print(0)
else:
    print("%.2f"%(totalAV/contAV))
    