import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    c = int(input_data[0])

    idx = 1
    for _ in range(c):
        p1 = input_data[idx]
        p2 = input_data[idx + 1]
        p_incompleta = input_data[idx + 2]
        idx += 3

        posicoes_ocultas = []
        for i in range(len(p_incompleta)):
            if p_incompleta[i] == '_':
                posicoes_ocultas.append(i)

        pos1 = posicoes_ocultas[0]
        pos2 = posicoes_ocultas[1]

        if (p1[pos1] == p2[pos2]) or (p1[pos2] == p2[pos1]):
            print("Y")
        else:
            print("N")

if __name__ == '__main__':
    main()