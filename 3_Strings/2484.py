import sys

for linha in sys.stdin:
    palavra = linha.strip()
    if not palavra:
        continue

    tamanho = len(palavra)

    for i in range(tamanho):
        espacos_iniciais = " " * i
        subpalavra = palavra[:tamanho - i]
        letras_separadas = " ".join(subpalavra)

        print(f"{espacos_iniciais}{letras_separadas}")

    print()