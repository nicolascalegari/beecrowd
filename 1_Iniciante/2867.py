import sys

def main():

    input_data = sys.stdin.read().split()

    if not input_data:
        return

    c = int(input_data[0])

    idx = 1

    for _ in range(c):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2

        resultado = n ** m

        digitos = len(str(resultado))

        print(digitos)

if __name__ == '__main__':
    main()
                   