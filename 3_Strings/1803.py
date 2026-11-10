import sys

def main():
    linhas = sys.stdin.read().splitlines()
    if not linhas or len(linhas) < 4:
        return

    num_colunas = len(linhas[0])

    valores_colunas = []

    for col in range(num_colunas):
        digitos = linhas[0][col] + linhas[1][col] + linhas[2][col] + linhas[3][col]
        valores_colunas.append(int(digitos))

    F = valores_colunas[0]
    L = valores_colunas[-1]

    mensagem_decodificada = []
    for i in range(1, num_colunas - 1):
        M_i = valores_colunas[i]
        C_i = (F * M_i + L) % 257
        mensagem_decodificada.append(chr(C_i))

    print("".join(mensagem_decodificada))

if __name__ == '__main__':
    main()