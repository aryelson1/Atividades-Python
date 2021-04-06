while True:
    primo = 1
    n = int(input())
    if n == -1:
        break
    if n <= 1:
        print(0)
        continue
    for i in range(2,n):
        if n % i == 0:
            primo = 0

    print(primo)
            