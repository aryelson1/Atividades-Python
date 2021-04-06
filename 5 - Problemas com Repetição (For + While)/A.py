cont = 1 
letras = ''
n = int(input())

for i in range(1,n+1):
    for j in range(1, cont+1):
        if j == cont:
            print(j, end = "");
        else:
            print(j, end = " ");
    print()
    cont+=1