ds = input()
preco = float(input())
op = input()
nome = input()

if (ds == "seg" or ds == "ter" or ds == "qua") and op == "ouro":
    preco = preco / 2
elif (ds == "qui" or ds == "sex") and 10 <= preco <= 100:
    preco = preco / 3
elif ds == "sab" and op == "prata":
    preco = preco * 3
else:
    preco = preco * 2


print("O preco do produto %s no dia %s eh %.2f"%(nome,ds,preco))