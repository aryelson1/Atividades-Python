def jogo():
    lista = []
    for i in range(10):
        lista.append(input())
    return lista


def verifica():
    resultado = []
    for i in range(0,10,2):
        if jogos[i] != jogos[i+1]:
            if jogos[i] == "papel":
                if jogos[i+1] == "tesoura":
                    resultado.append(1)
                else:
                    resultado.append(0)
                    
            elif jogos[i] == "pedra" :
                if jogos[i+1] == "papel":
                    resultado.append(1)
                else:
                    resultado.append(0)
            else:
                if jogos[i+1] == "pedra":
                    resultado.append(1)
                else:
                    resultado.append(0)
        else:
            resultado.append(2)
    return resultado
    
while True:
    jogos = jogo()
    result = verifica()
    if result.count(0) < result.count(1):
        print("MIGUEL")
        break
    elif result.count(0) > result.count(1):
        print("MARIA RITA")
        break