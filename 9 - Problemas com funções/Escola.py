def ClassificaAluno(media,faltas):
    if faltas < 11:
        if media >= 7.0:
            if media > 9.4:
                return "APROVADO COM LOUVOR"
            else:
                return "APROVADO"
        else:
            return "REPROVADO"
    else:
        return "REPROVADO POR FALTAS"

media = float(input())
faltas = int(input())

print(ClassificaAluno(media,faltas))