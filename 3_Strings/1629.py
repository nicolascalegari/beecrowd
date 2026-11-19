import sys

def somar_digitos(n):

    return sum(int(digito) for digito in str(n))

def resolver():

    linhas = sys.stdin.read().splitlines()
    idx = 0

    while idx < len(linhas):
        linha_n = linhas[idx].strip()
        if not linha_n:
            idx += 1
            continue

        n = int(linha_n)
        if n == 0:
            break
        idx += 1

        for _ in range(n):
            string_compactada = linhas[idx].strip()
            idx += 1

            total_zeros = 0
            total_uns = 0

            for i, digito_char in enumerate(string_compactada):
                quantidade = int(digito_char)
                if i % 2 == 0:
                    total_zeros += quantidade
                else:
                    total_uns += quantidade

            digito_verificador = somar_digitos(total_zeros) + somar_digitos(total_uns)
            print(digito_verificador)

if __name__ == '__main__':
    resolver()