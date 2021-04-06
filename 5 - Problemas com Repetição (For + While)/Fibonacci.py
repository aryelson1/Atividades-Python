while True:
    numero = int(input())
    if numero == 0:
        break
    elif numero == 1:
        print("0")
    elif numero == 2:
        print("0 1")
    else:
        numero1 = 0
        numero2 = 1
        print("0 1", end = " ")
        for i in range(numero - 2):
            numero3 = numero1 + numero2
            numero1 = numero2
            numero2 = numero3
            if i == numero - 3:
                print(numero3)
            else:
                print(numero3, end = " ")