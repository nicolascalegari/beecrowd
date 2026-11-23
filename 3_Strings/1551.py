n = int(input())

for _ in range(n):
    frase = input()

    letras_unicas = {caractere for caractere in frase if caractere.isalpha()}
    quantidade = len(letras_unicas)

    if quantidade == 26:
        print("frase completa")
    elif quantidade >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")