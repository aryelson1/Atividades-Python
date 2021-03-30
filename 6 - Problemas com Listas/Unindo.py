l1 = []

n = int(input())
if n > 0:
    for i in range(n):
        l1.append(int(input()))
    n = int(input())
    if n > 0:
        for i in range(n):
            l1.append(int(input()))
        for i in l1:
            print(i, end = " ")
    else:
      print("Erro - A lista deve ter pelo menos 1 elemento.")

else:
    print("Erro - A lista deve ter pelo menos 1 elemento.")