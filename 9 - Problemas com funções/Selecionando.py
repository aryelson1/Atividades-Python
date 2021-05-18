def classifica():
    if p.count(0) >= 2:
        titulares.append(0)
    else:
        titulares.append(p[0]*2 + p[1]*3.5 + p[2]*1.5 + p[3]*2)

titulares = []
for i in range(5):
    nome = input()
    p = []
    for j in range(4):
        p.append(int(input()))
    classifica()
    
titulares.sort()
print("%.1f"%titulares[4])
print("%.1f"%titulares[3])
print("%.1f"%titulares[2])