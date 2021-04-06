idade = int(input())
prof = int(input())
ec = input()
ri = input()

print("Sua idade:")
print("Profissao(1-saude;2-indigenas;3-professores;4-seguranca;5-sistema prisional; 6-outro):")
print("Tem comorbidades (s/n)?")
print("Mora em residencia institucionalizada(s/n)?")
print("--------------------------")

if prof > 6:
    print("Voce informou um codigo de profissao invalido")
elif prof == 1:
    print("Voce eh do grupo 1 e serah vacinado na Fase 1")
elif (idade >= 60 and ri == "s") or idade >= 75 or prof == 2:
    print("Voce eh do grupo 2 e serah vacinado na Fase 1")
elif idade >= 60:
    if idade <= 64:
        print("Voce eh do grupo 5 e serah vacinado na Fase 2")
    elif idade < 70:
        print("Voce eh do grupo 4 e serah vacinado na Fase 2")
    else:
        print("Voce eh do grupo 3 e serah vacinado na Fase 2")
elif ec == "s":
    print("Voce eh do grupo 6 e serah vacinado na Fase 3") 
else:
    if prof == 3:
        print("Voce eh do grupo 7 e serah vacinado na Fase 4")
    else:
        print("Voce eh do grupo 8 e serah vacinado na Fase 4")
