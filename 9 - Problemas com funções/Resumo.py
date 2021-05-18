def q(lado):
    if lado < 0:
        return -1
    else:
        return (lado**2)


def r(base,altura):
    if altura < 0 or base < 0:
        return -1
    else:
        return (base * altura)


def c(raio):
    if raio < 0:
        return -1
    else:
        return 3.14 * (raio ** 2)
        

qs = []
rs = []
cs = []

while True:
    caso = input()
    if caso == "sair":
        print("Maior circulo: %.2f" %max(cs))
        print("Maior retangulo: %.2f" %max(rs))
        print("Maior quadrado: %.2f"  %max(qs))
        print("Quantidade de figuras %d" %(len(cs)+len(rs)+len(qs)))
        print("Percentual de circulos: %.2f" %((len(cs) / (len(cs)+len(rs)+len(qs))) * 100))
        break
    elif caso == "q":
        lado = int(input())
        qs.append(q(lado))
    elif caso == "r":
        base = int(input())
        altura = int(input())
        rs.append(r(base, altura))
    else:
        raio = int(input())
        cs.append(c(raio))
        

