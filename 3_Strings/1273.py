def justificar_palavras():
    primeiro_caso = True

    while True:
        quantidade_palavras = int(input())

        if quantidade_palavras == 0:
            break

        if not primeiro_caso:
            print()
        else:
            primeiro_caso = False

        palavras = []
        comprimento_maximo = 0

        for _ in range(quantidade_palavras):
            palavra = input().strip()
            palavras.append(palavra)
            if len(palavra) > comprimento_maximo:
                comprimento_maximo = len(palavra)

        for palavra in palavras:
            print(palavra.rjust(comprimento_maximo))

if __name__ == '__main__':
    justificar_palavras()