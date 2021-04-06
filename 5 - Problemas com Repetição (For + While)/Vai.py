cidade = ''
distR = 0
while True:
    nome = input().upper()
    if nome == "FIM":
        break
    distancia = int(input())
    valor = float(input())
    if distancia > distR and valor*2 <= 300:
        cidade = nome
        distR = distancia

if distR == 0:
    print("SEM DESTINO")
else:
    print(cidade)