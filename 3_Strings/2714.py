import sys

def resolver():
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return

    n = int(linhas[0])

    for i in range(1, n + 1):
        ra = linhas[i]

        if len(ra) == 20 and ra.startswith("RA") and ra[2:].isdigit():
            parte_numerica = ra[2:]
            senha = parte_numerica.lstrip('0')

            if senha:
                print(senha)
            else:
                print("INVALID DATA")
        else:
            print("INVALID DATA")

if __name__ == '__main__':
    resolver()