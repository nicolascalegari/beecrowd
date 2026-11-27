import sys

def resolver():
    tabela = str.maketrans("@&!*#", "aeiou")

    for linha in sys.stdin:
        frase_decodificada = linha.rstrip('\r\n').translate(tabela)
        print(frase_decodificada)

if __name__ == '__main__':
    resolver()