import sys

def main():
    entrada = sys.stdin.read().splitlines()
    if not entrada:
        return

    n = int(entrada[0].strip())

    indice_linha = 1
    for _ in range(n):
        if indice_linha >= len(entrada):
            break

        k = int(entrada[indice_linha].strip())
        indice_linha += 1

        primeiro_idioma = entrada[indice_linha].strip()

        all_same = True

        for i in range(k):
            idioma_atual = entrada[indice_linha + i].strip()
            if idioma_atual != primeiro_idioma:
                all_same = False


        indice_linha += k

        if all_same:
            print(primeiro_idioma)
        else:
            print("ingles")

if __name__ == '__main__':
    main()
