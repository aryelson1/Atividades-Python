cont = 0
while True:
    QP = int(input())
    if QP < 0 :
        break
    QM = int(input())
    R = float(input())
    if QP >= 40 and QM >= 21 and R >= 7.0:
        cont += 1
print(cont)