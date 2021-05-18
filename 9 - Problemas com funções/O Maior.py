def maior(nms):
    nms = list(map(int,nms))
    nms.sort()
    print(nms[-1],"eh o maior ")


nms = input().split()
maior(nms)