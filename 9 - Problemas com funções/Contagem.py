def imprime(n):
    for i in range(n,0,-1):
        for j in range(n):
            if j == n-1:
                print(i)
            else:
                print(i, end = '-')
        n -= 1
        
        
n = int(input())
imprime(n)
