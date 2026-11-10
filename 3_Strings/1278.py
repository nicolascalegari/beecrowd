import sys

def main():
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return

    idx = 0
    primeiro_caso = True

    while idx < len(linhas):
        if not linhas[idx].strip():
            idx += 1
            continue

        n = int(linhas[idx].strip())
        if n == 0:
            break

        if not primeiro_caso:
            print()
        primeiro_caso = False

        idx += 1
        casos_limpos = []
        max_len = 0

        for _ in range(n):
            palavras = linhas[idx].split()
            linha_limpa = " ".join(palavras)
            casos_limpos.append(linha_limpa)

            if len(linha_limpa) > max_len:
                max_len = len(linha_limpa)
            idx += 1

        for linha in casos_limpos:
            print(linha.rjust(max_len))

if __name__ == "__main__":
    main()