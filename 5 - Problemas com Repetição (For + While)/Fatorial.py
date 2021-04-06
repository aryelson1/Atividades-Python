while True :
    F = 1
    No = int (input())
        
    if No == -1:
        break
    while No > 1:
        F = F * No
        No = No - 1
    print (F)
