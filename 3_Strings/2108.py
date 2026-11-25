maior_palavra = ""

while True:
    linha = input()

    if linha == "0":
        break

    palavras = linha.split(" ")
    tamanhos = []

    for palavra in palavras:
        tamanho = len(palavra)
        tamanhos.append(str(tamanho))

        if tamanho >= len(maior_palavra):
            maior_palavra = palavra

    print("-".join(tamanhos))

print()
print(f"The biggest word: {maior_palavra}")