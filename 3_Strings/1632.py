import sys

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    t = int(input_data[0].strip())

    letras_especiais = {'a', 'e', 'i', 'o', 's'}

    for i in range(1, t + 1):
        senha = input_data[i].strip().lower()
        variacoes = 1

        for caractere in senha:
            if caractere in letras_especiais:
                variacoes *= 3
            else:
                variacoes *= 2

        print(variacoes)

if __name__ == '__main__':
    main()