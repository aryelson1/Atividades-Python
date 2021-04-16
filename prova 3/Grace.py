while True:
    palavra = input().upper()
    cont = 0
    if palavra == "FIM":
        break
    palavras = palavra.split("-")
    p = 0
    for i in palavras:
        if p == 0:
            if i[0] == "C" or i[-1] == "C":
                cont += 1
        elif p == 1:
            if i[0] == "O" or i[-1] == "0":
                cont += 1
        elif p == 2:
            if i[0] == "B" or i[-1] == "B":
                cont += 1
        elif p == 3:
            if i[0] == "O" or i[-1] == "O":
                cont += 1
        elif p == 4:
            if i[0] == "L" or i[-1] == "L":
                cont += 1
        p += 1
    if cont > 4:
        print("GRACE HOPPER")
    else:
        print("BUG")
    cont = 0
        