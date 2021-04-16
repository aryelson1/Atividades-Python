while True:
    palavra = input().upper()
    cont = 0
    if palavra == "FIM":
        break
    palavras = palavra.split("-")
    p = 0
    for i in palavras:
        if (i[0] == "C" or i[-1] == "C") and p == 0:
                cont += 1
        elif (i[0] == "O" or i[-1] == "0") and p == 1:
                cont += 1
        elif (i[0] == "B" or i[-1] == "B") and p == 2:
                cont += 1
        elif (i[0] == "O" or i[-1] == "O") and p == 3:
                cont += 1
        elif i[0] == "L" or i[-1] == "L":
                cont += 1
        p += 1
    print("GRACE HOPPER") if cont > 4 else  print("BUG")
    cont = 0
