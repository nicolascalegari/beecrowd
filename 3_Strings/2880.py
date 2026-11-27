import sys

def resolver():
    entrada = sys.stdin.read().splitlines()
    if len(entrada) < 2:
        return

    cifrada = entrada[0].strip()
    crib = entrada[1].strip()

    tam_cifrada = len(cifrada)
    tam_crib = len(crib)
    posicoes_validas = 0

    for i in range(tam_cifrada - tam_crib + 1):
        valido = True

        for j in range(tam_crib):
            if cifrada[i + j] == crib[j]:
                valido = False
                break

        if valido:
            posicoes_validas += 1

    print(posicoes_validas)

if __name__ == '__main__':
    resolver()