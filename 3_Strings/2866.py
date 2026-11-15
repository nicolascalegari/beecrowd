import sys

def resolver():
    linhas = sys.stdin.read().splitlines()
    if not list(linhas):
        return

    c = int(linhas[0])

    for i in range(1, c + 1):
        texto_codificado = linhas[i]
        letras_minusculas = [char for char in texto_codificado if char.islower()]
        texto_oculto = "".join(letras_minusculas[::-1])
        print(texto_oculto)

if __name__ == "__main__":
    resolver()