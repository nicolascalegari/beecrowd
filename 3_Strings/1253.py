import sys

def resolver():

    entrada = sys.stdin.read().splitlines()
    if not entrada:
        return

    num_casos = int(entrada[0])

    linha_atual = 1

    for _ in range(num_casos):
        texto_codificado = entrada[linha_atual]
        deslocamento = int(entrada[linha_atual + 1])

        texto_original = []

        for letra in texto_codificado:
            posicao_atual = ord(letra) - ord('A')
            nova_posicao = (posicao_atual - deslocamento) % 26
            letra_original = chr(nova_posicao + ord('A'))
            texto_original.append(letra_original)

        print("".join(texto_original))
        linha_atual += 2

if __name__ == '__main__':
    resolver()