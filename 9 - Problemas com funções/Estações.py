def estacao(dia,mes):
    if mes < 4 or (mes == 4 and dia < 21):
        return "VERAO"
    elif mes < 6 or (mes == 6 and dia < 21):
        return "OUTONO"
    elif mes < 9 or (mes == 6 and dia < 21):
        return "INVERNO"
    else:
        return "PRIMAVERA"


dia = int(input())
mes = int(input())

print(estacao(dia,mes))