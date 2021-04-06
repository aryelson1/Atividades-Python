level = int(input())

if level <= 20:
    a = (20 + (level)**3)
elif level <= 40:
    a= (8000 + (level - 10)**2)
elif level <= 60:
    a = (9000 + 5*level)
elif level <= 80:
    a = (9300 + 2*level)
else:
    a = 9500 + level
	
	
print("Potencia de : %i W"%a)
	