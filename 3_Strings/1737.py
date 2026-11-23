import sys
from collections import Counter

def resolver():
    linhas_entrada = sys.stdin.read().splitlines()
    indice = 0
    total_linhas = len(linhas_entrada)

    while indice < total_linhas:
        # Ignora possíveis linhas vazias antes de ler o número n
        linha_n = linhas_entrada[indice].strip()
        indice += 1
        if not linha_n:
            continue

        n = int(linha_n)
        if n == 0:
            break

        # Lê as próximas n linhas e concatena sem quebras de linha
        partes_texto = []
        for _ in range(n):
            if indice < total_linhas:
                partes_texto.append(linhas_entrada[indice])
                indice += 1

        texto = "".join(partes_texto)
        total_digrafos = len(texto) - 1

        if total_digrafos <= 0:
            print()
            continue

        # Extrai todos os pares consecutivos e conta suas ocorrências
        digrafos = (texto[i:i+2] for i in range(total_digrafos))
        contagem = Counter(digrafos)

        # Ordena: maior frequência (-x[1]) primeiro, depois ordem ASCII (x[0])
        ordenados = sorted(contagem.items(), key=lambda x: (-x[1], x[0]))

        # Imprime os 5 mais frequentes
        for digrafo, freq in ordenados[:5]:
            freq_relativa = freq / total_digrafos
            print(f"{digrafo} {freq} {freq_relativa:.6f}")

        print()

if __name__ == "__main__":
    resolver()
