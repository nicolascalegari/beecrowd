while True:
    try:
        vogais = input()
        frase = input()
        contador = 0

        for letra in frase:
            if letra in vogais:
                contador += 1

        print(contador)

    except EOFError:
        break