import sys

dados = sys.stdin.read().splitlines()

if dados:
    c = int(dados[0].strip())
    indice = 1

    for _ in range(c):
        n = int(dados[indice].strip())
        indice += 1

        posses = set()

        for _ in range(n):
            linha = dados[indice].strip()
            indice += 1

            coisa, comando = linha.rsplit(maxsplit=1)

            if comando == "chirrin":
                posses.add(coisa)
            elif comando == "chirrion":
                posses.discard(coisa)

        print("TOTAL")
        for item in sorted(posses):
            print(item)
