import sys

PALAVRAS = ["be", "our", "rum", "will", "dead", "hook",
            "ship", "blood", "sable", "avenge", "parrot", "captain"]

def main():
    texto = sys.stdin.readline().rstrip("\n")
    cifradas = list(set(texto.split()))
    letras_cifradas = set(c for c in texto if c != " ")
    total = len(letras_cifradas)

    resultados = set()
    mapa = {}      # cifrada -> simples
    inverso = {}   # simples -> cifrada

    def decodificar():
        return "".join(mapa[c] if c != " " else " " for c in texto)

    def busca(i, usadas):
        if len(resultados) > 1:
            return
        if i == len(PALAVRAS):
            if len(mapa) == total:
                resultados.add(decodificar())
            return
        # opção 1: palavra conhecida não é usada
        busca(i + 1, usadas)
        # opção 2: associa a uma palavra cifrada
        p = PALAVRAS[i]
        for w in cifradas:
            if w in usadas or len(w) != len(p):
                continue
            adicionadas = []
            ok = True
            for a, b in zip(w, p):
                if a in mapa:
                    if mapa[a] != b:
                        ok = False
                        break
                elif b in inverso:
                    ok = False
                    break
                else:
                    mapa[a] = b
                    inverso[b] = a
                    adicionadas.append(a)
            if ok:
                usadas.add(w)
                busca(i + 1, usadas)
                usadas.discard(w)
            for a in adicionadas:
                del inverso[mapa[a]]
                del mapa[a]

    busca(0, set())

    if len(resultados) == 1:
        print(next(iter(resultados)))
    else:
        print("Impossible")

main()