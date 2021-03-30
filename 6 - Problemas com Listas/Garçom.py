n = int(input())
cont = 0
for i in range(n):
    l = input().split()
    l = list(map(int,l))
    if l[0] > l[1]:
        cont += l[1]
print(cont)
