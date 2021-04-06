nome = input()


if nome != "Homem de Ferro" and nome != "Capit�o Am�rica" and nome != "Hulk" and nome != "Thor" and nome != "Gavi�o Arqueiro" and nome != "Vi�va Negra" :
    print("Vingador Inv�lido")
else:
    atk = input()
    energia = int(input())
    if nome == "Capit�o Am�rica":
        if atk == "Escudo" :
            if energia >= 7:
                print("%s conseguiu derrotar Thanos"%nome)
            else:
                print("%s NAO conseguiu derrotar Thanos, chamem outro Vingador"%nome)
        elif atk == "Armadura de Ferro":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Homem de Ferro"%nome)
        elif atk == "For�a Bruta":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Hulk"%nome)
        elif atk == "Martelo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Thor"%nome)
        elif atk == "Arco e Flecha":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Gavi�o Arqueiro"%nome)
        else:
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder da Vi�va Negra"%nome)
    elif nome == "Homem de Ferro":
        if atk == "Armadura de Ferro" :
            if energia >= 10:
                print("%s conseguiu derrotar Thanos"%nome)
            else:
                print("%s NAO conseguiu derrotar Thanos, chamem outro Vingador"%nome)
        elif atk == "Escudo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Capit�o Am�rica"%nome)
        elif atk == "For�a Bruta":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Hulk"%nome)
        elif atk == "Martelo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Thor"%nome)
        elif atk == "Arco e Flecha":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Gavi�o Arqueiro"%nome)
        else:
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder da Vi�va Negra"%nome)
    elif nome == "Hulk":
        if atk == "For�a Bruta" :
            if energia >= 5:
                print("%s conseguiu derrotar Thanos"%nome)
            else:
                print("%s NAO conseguiu derrotar Thanos, chamem outro Vingador"%nome)
        elif atk == "Escudo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Capit�o Am�rica"%nome)
        elif atk == "Armadura de Ferro":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Homem de Ferro"%nome)
        elif atk == "Martelo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Thor"%nome)
        elif atk == "Arco e Flecha":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Gavi�o Arqueiro"%nome)
        else:
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder da Vi�va Negra"%nome)
    elif nome == "Thor":
        if atk == "Martelo" :
            if energia >= 4:
                print("%s conseguiu derrotar Thanos"%nome)
            else:
                print("%s NAO conseguiu derrotar Thanos, chamem outro Vingador"%nome)
        elif atk == "Escudo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Capit�o Am�rica"%nome)
        elif atk == "Armadura de Ferro":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Homem de Ferro"%nome)
        elif atk == "For�a Bruta":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Hulk"%nome)
        elif atk == "Arco e Flecha":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Gavi�o Arqueiro"%nome)
        else:
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder da Vi�va Negra"%nome)
    elif nome == "Gavi�o Arqueiro":
        if atk == "Arco e Flecha" :
            if energia >= 12:
                print("%s conseguiu derrotar Thanos"%nome)
            else:
                print("%s NAO conseguiu derrotar Thanos, chamem outro Vingador"%nome)
        elif atk == "Escudo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Capit�o Am�rica"%nome)
        elif atk == "Armadura de Ferro":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Homem de Ferro"%nome)
        elif atk == "Martelo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Thor"%nome)
        elif atk == "For�a Bruta":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Hulk"%nome)
        else:
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder da Vi�va Negra"%nome)
    else:
        if atk == "Intelig�ncia" :
            if energia >= 20:
                print("%s conseguiu derrotar Thanos"%nome)
            else:
                print("%s NAO conseguiu derrotar Thanos, chamem outro Vingador"%nome)
        elif atk == "Escudo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Capit�o Am�rica"%nome)
        elif atk == "Armadura de Ferro":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Homem de Ferro"%nome)
        elif atk == "Martelo":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Thor"%nome)
        elif atk == "For�a Bruta":
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Hulk"%nome)
        else:
            print("%s NAO conseguiu derrotar Thanos\nEsse � o poder do Gavi�o Arqueiro"%nome)