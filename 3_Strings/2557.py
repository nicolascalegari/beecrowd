import sys

def resolver():
    linhas = sys.stdin.read().splitlines()

    for linha in linhas:
        if not linha.strip():
            continue

        parte_esquerda, j_str = linha.split('=')
        r_str, l_str = parte_esquerda.split('+')

        if r_str == 'R':
            l = int(l_str)
            j = int(j_str)
            print(j - l)
        elif l_str == 'L':
            r = int(r_str)
            j = int(j_str)
            print(j - r)
        elif j_str == 'J':
            r = int(r_str)
            l = int(l_str)
            print(r + l)

if __name__ == "__main__":
    resolver()