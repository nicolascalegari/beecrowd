import sys

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    v = int(input_data[0])
    n = int(input_data[1])

    total_placas = v * n
    resultados = []

    for i in range(1, 10):
        placas_necessarias = (i * total_placas + 9) // 10
        resultados.append(str(placas_necessarias))

    print(" ".join(resultados))

if __name__ == '__main__':
    main()