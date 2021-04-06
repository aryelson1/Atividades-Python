idade = int(input())
jogo = input()

if idade < 0 or idade > 130:
    print("Idade invalida." )
elif jogo != "azar" and jogo != "mmorpg" and jogo != "moba" and jogo != "casual":
    print("Jogo invalido.")
elif idade >= 21 and jogo == "azar":
    print("Pode entrar!")
elif idade >= 14 and jogo == "mmorpg":
    print("Pode entrar!")
elif idade >= 10 and jogo == "moba":
    print("Pode entrar!")
elif jogo == "casual":
    print("Pode entrar!")
else:
    print("Volte daqui h� alguns anos.")