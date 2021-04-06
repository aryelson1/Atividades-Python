divida = int(input())
mensal = int(input())
while True:
    print("(antes)",divida)
    if divida-mensal <= 0:
        print("(depois) 0")
        break
    else:
        print("(depois)",divida-mensal)
    
    divida -= mensal