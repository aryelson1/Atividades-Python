escala = input ()
valor = float (input())

if ((escala == "C" and valor >= -273.0) or (escala == "F" and valor >= -459.67) or (escala == "K" and valor >= 0.0)):
    if (escala == "C"):
        convert_fahrenheit = float( 1.8*valor + 32)
        convert_kelvin = float (valor + 273.15)
        print ("%.2f F" %convert_fahrenheit)
        print ("%.2f K" %convert_kelvin)

    elif (escala == "F"):
        convert_celsius = float ( (valor - 32) / 1.8)
        convert_kelvin = float ( (valor-32)*0.555 + 273.15)
        print ("%.2f C"%convert_celsius)
        print ("%.2f K"%convert_kelvin)
    
    elif (escala == "K"):
        convert_fahrenheit = (1.8*(valor - 273.15) + 32)
        convert_celsius = valor - 273.15
        print ("%.2f C"%convert_celsius)
        print ("%.2f F"%convert_fahrenheit)
        
else:   print ("Valor de temperatura abaixo do minimo")