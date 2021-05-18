def codifica(nome):
    letras ="aeiots" 
    cods = "@31075"
    for i in range(len(letras)):
        nome = nome.replace(letras[i],cods[i])
        nome = nome.replace(letras[i].upper(),cods[i])
    return nome
    
def contsubs(nome):
    letras ="aeiotsAEIOTS" 
    cont = 0
    for i in letras:
        if i in nome:
            cont += nome.count(i)
    return cont
    
def MensErro(nome):
    if nome == "":
        print("Estamos com problemas na conex?o com o servidor")
    else:
        print("numeros")
        print(0)
def isnumero(nome):
    for i in nome:
        if i.isdigit():
            return True
    return False

nome = input()[::-1]

if isnumero(nome) or nome == "":
    MensErro(nome)
else:
    print(codifica(nome))
    print(contsubs(nome))
