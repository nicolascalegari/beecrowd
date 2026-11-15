import sys

def resolver():
    entrada = sys.stdin.read().strip()
    if not entrada:
        return

    palavras = entrada.split()
    palavras_corrigidas = []

    for palavra in palavras:
        if len(palavra) >= 4 and palavra[0:2] == palavra[2:4]:
            palavras_corrigidas.append(palavra[2:])
        else:
            palavras_corrigidas.append(palavra)

    print(" ".join(palavras_corrigidas))

if __name__ == '__main__':
    resolver()