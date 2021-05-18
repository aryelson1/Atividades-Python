def calcula(entrada):
    maior = []
    for i in entrada:
        linha = []
        for j in i:
            linha.append(int(j))
        maior.append(max(linha))
    
    return sum(maior)%10
    
def verifica(digito):
    if digito == int(entrada[-1]):
        print("VALIDO")
    else:
        print("INVALIDO")
    
while True:
    entrada = input()
    if entrada.upper() == "FIM":
        break
    entrada = entrada.replace("-",".")
    entrada = entrada.split(".")
    verifica(calcula(entrada[0:3]))