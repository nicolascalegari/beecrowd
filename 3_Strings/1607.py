import sys

def resolver():
    entrada = sys.stdin.read().splitlines()

    if not entrada:
        return

    t = int(entrada[0])

    for i in range(1, t + 1):
        if i > len(entrada):
            break

        partes = entrada[i].split()
        if len(partes) < 2:
            continue

        str_a, str_b = partes[0], partes[1]
        total_operacoes = 0

        for char_a, char_b in zip(str_a, str_b):
            distancia = (ord(char_b) - ord(char_a)) % 26
            total_operacoes += distancia

        print(total_operacoes)

if __name__ == '__main__':
    resolver()