import sys

def resolver():

    linhas = [linha.rstrip('\r\n') for linha in sys.stdin]

    # Processa de 3 em 3 linhas até o fim da entrada (EOF)
    for i in range(0, len(linhas), 3):
        if i + 2 >= len(linhas):
            break

        tag_alvo = linhas[i]
        novo_valor = linhas[i + 1]
        texto = linhas[i + 2]

        tag_alvo_lower = tag_alvo.lower()
        tam_alvo = len(tag_alvo)

        resultado = []
        dentro_de_tag = False
        idx = 0
        n = len(texto)

        while idx < n:
            char = texto[idx]

            # Controla se entramos ou saímos de uma tag <...>
            if char == '<':
                dentro_de_tag = True
                resultado.append(char)
                idx += 1
            elif char == '>':
                dentro_de_tag = False
                resultado.append(char)
                idx += 1
            else:
                # Se estamos dentro de uma tag, verificamos se a substring atual bate com o alvo
                if (
                    dentro_de_tag
                    and texto[idx : idx + tam_alvo].lower() == tag_alvo_lower
                ):
                    resultado.append(novo_valor)
                    idx += tam_alvo  # Pula o tamanho da palavra substituída
                else:
                    resultado.append(char)
                    idx += 1

        print(''.join(resultado))

if __name__ == '__main__':
    resolver()