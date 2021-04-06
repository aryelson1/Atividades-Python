quant = int(input())
cidade = input().upper()
quartos  = int(input())

if cidade == "PIPA":
    if quartos <= 2:
        total = (quant*75) + (600)
    else:
        total = (quant*75) + (900)
else:
    if quartos <= 3:
        total = (quant*60) + (950)
    else:
        total = (quant*60) + (1120)

print("%.2f" %total)
print("%.2f"%(total/quant))