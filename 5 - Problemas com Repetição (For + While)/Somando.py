n1 = int(input())
n2 = int(input())
s = 0
if n2 > 0:
    for i in range(1,n2+1):
        s += i
elif n1 > 0:
    for i in range(1,n1+1):
        s += i
print(s)