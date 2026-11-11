import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    c = int(input_data[0])

    idx = 1
    for _ in range(c):
        if idx >= len(input_data):
            break

        b = int(input_data[idx])
        e = int(input_data[idx + 1])
        idx += 2

        sequencia = []
        for i in range(b, e + 1):
            sequencia.append(str(i))

        parte_normal = "".join(sequencia)
        parte_espelhada = parte_normal[::-1]
        resultado_final = parte_normal + parte_espelhada
        print(resultado_final)

if __name__ == '__main__':
    main()