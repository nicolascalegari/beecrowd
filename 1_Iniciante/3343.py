import sys

def resolver():

    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    x = int(input_data[1])

    ordem_titas = input_data[2]

    p = int(input_data[3])
    m = int(input_data[4])
    g = int(input_data[5])

    tamanhos = {"P": p, "M": m, "G": g}

    muralhas = []

    indices_busca = {"P": 0, "M": 0, "G": 0}

    for tita in ordem_titas:
        tam_tita = tamanhos[tita]

        idx = indices_busca[tita]

        while idx < len(muralhas) and muralhas[idx] < tam_tita:
            idx += 1

        indices_busca[tita] = idx

        if idx == len(muralhas):
            muralhas.append(x)

        muralhas[idx] -= tam_tita

    print(len(muralhas))

if __name__ == "__main__":
    resolver()
