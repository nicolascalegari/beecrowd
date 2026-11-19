import sys

def resolver():
    linhas = sys.stdin.read().splitlines()
    idx = 0

    while idx < len(linhas):
        if not linhas[idx].strip():
            idx += 1
            continue

        n, m = map(int, linhas[idx].split())
        if n == 0 and m == 0:
            break
        idx += 1

        desenho = [linhas[idx + i] for i in range(n)]
        idx += n

        a, b = map(int, linhas[idx].split())
        idx += 1

        fator_linha = a // n
        fator_coluna = b // m

        for linha in desenho:

            linha_ampliada = "".join(char * fator_coluna for char in linha)

            for _ in range(fator_linha):
                print(linha_ampliada)

        print()

if __name__ == "__main__":
    resolver()
