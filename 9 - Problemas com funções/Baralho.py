def crescente():
    if cartas[0]+1 == cartas[1] and cartas[1]+1 == cartas[2] :
        pontuacao.append(min(cartas))
    iguais()

def iguais():
    if cartas[0] == cartas[1] == cartas[2]:
        pontuacao.append(min(cartas))
    menores()
    
def menores():
    verf = cartas.copy()
    verf.remove(max(cartas))
    if verf[0] == verf[1] and verf[0] != max(cartas):
        pontuacao.append(verf[0]//2)
    maiores()
    
def maiores():
    verf = cartas.copy()
    verf.remove(min(cartas))
    if verf[0] == verf[1] and  verf[0] != min(cartas):
        pontuacao.append(verf[0]//2)
    iguais8()
    
def iguais8():
    if sum(cartas) == 8:
        pontuacao.append(8)
    
cartas = input().split()
cartas = list(map(int,cartas))
cartas.sort()
pontuacao = []
crescente()
n1 = sum(pontuacao)

cartas = input().split()
cartas = list(map(int,cartas))
cartas.sort()
pontuacao = []
crescente()
n2 = sum(pontuacao)

if n1 == n2:
    print(0)
elif n1 > n2:
    print(1)
else:
    print(2)
