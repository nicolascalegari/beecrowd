import sys

def main():
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return

    idx = 0
    while idx < len(linhas):
        t = int(linhas[idx])
        idx += 1

        expressoes = []
        for _ in range(t):
            partes = linhas[idx].replace('=', ' ').split()
            x = int(partes[0])
            y = int(partes[1])
            z = int(partes[2])
            expressoes.append((x, y, z))
            idx += 1

        errou = []
        for _ in range(t):
            nome, e_idx, operacao = linhas[idx].split()
            e_idx = int(e_idx) - 1
            idx += 1

            x, y, z = expressoes[e_idx]

            correto = False
            if operacao == '+':
                correto = (x + y == z)
            elif operacao == '-':
                correto = (x - y == z)
            elif operacao == '*':
                correto = (x * y == z)
            elif operacao == 'I':
                correto = (x + y != z) and (x - y != z) and (x * y != z)

            if not correto:
                errou.append(nome)

        if len(errou) == 0:
            print("You Shall All Pass!")
        elif len(errou) == t:
            print("None Shall Pass!")
        else:
            errou.sort()
            print(" ".join(errou))

if __name__ == "__main__":
    main()