totalG = 0
totalP = 0
for i in range(7):
    quant = int(input())
    tamanho = input().upper()
    if tamanho == "G":
        totalG += quant
    else:
        totalP += quant
print(totalG*16 + totalP*10)
print( int(((totalG*16 + totalP*10)*2)/7 ))