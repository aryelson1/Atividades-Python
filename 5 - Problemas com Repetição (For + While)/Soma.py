soma = 0
msoma= 0


for c in range(5):
    m = int(input())
    for i in range(1, m+1):
        if m % i == 0:
            soma = soma+i
    if soma > msoma:
        msoma = soma
        divi = m
    soma = 0
  
print(divi)