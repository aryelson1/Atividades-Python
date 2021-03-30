n = int(input())
if n > 0:
    l = [float(input()) for i in range(n)]

    for i in range(n):
        print("Nota %d: %.1f"%(i+1,l[i]))
    print("Media: %.2f"%(sum(l)/len(l)))
else:
    print("Numero de notas invalido.")
    