import sys

def resolver():
    caso = 1

    for linha in sys.stdin:
        s = linha.strip()

        if s == '*':
            break
        if not s:
            continue

        n = len(s)
        dupla = s + s

        menor = s
        maior = s

        for i in range(1, n):
            rotacao = dupla[i : i + n]
            if rotacao < menor:
                menor = rotacao
            elif rotacao > maior:
                maior = rotacao

        print(f"Caso {caso}: {menor} {maior}")
        caso += 1

if __name__ == '__main__':
    resolver()