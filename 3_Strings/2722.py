n = int(input())

for _ in range(n):

    linha1 = input()
    linha2 = input()

    nome_correto = ""

    for i in range(0, len(linha1), 2):

        nome_correto += linha1[i:i + 2] + linha2[i:i + 2]

    print(nome_correto)