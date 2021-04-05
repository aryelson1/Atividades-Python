while True:
    n = input()
    if n == "0":
        break
    nome = input()
    palavrai = ""
    for letra in nome:
            palavrai = letra + palavrai
    print(palavrai)
