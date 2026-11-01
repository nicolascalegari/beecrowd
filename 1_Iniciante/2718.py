import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    for i in range(1, n + 1):
        x = int(input_data[i])

        binario = bin(x)[2:]
        grupos_de_uns = binario.split('0')
        maior_sequencia = max(len(grupo) for grupo in grupos_de_uns)

        print(maior_sequencia)

if __name__ == '__main__':
    main()