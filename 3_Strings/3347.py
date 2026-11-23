import sys

def resolver():

    dados = sys.stdin.read().split()
    if not dados:
        return

    n = int(dados[0])
    qtd_p = int(dados[1])

    # As próximas qtd_p strings são as populações P
    populacoes = dados[2 : 2 + qtd_p]
    # A última string é o genoma G
    genoma_g = dados[2 + qtd_p]

    resultados = []
    i = 0

    while i < n:
        melhor_tamanho = 0
        melhor_id = -1

        # Testa cada população de 0 a qtd_p - 1 (garante o menor índice em caso de empate)
        for idx, pop in enumerate(populacoes):
            tamanho = 0
            while i + tamanho < n and pop[i + tamanho] == genoma_g[i + tamanho]:
                tamanho += 1

            if tamanho > melhor_tamanho:
                melhor_tamanho = tamanho
                melhor_id = idx + 1  # Índices na saída começam em 1

        # Se nenhuma população coincidiu na posição i
        if melhor_tamanho == 0:
            resultados.append(f"{genoma_g[i]} -1")
            i += 1
        else:
            trecho = genoma_g[i : i + melhor_tamanho]
            resultados.append(f"{trecho} {melhor_id}")
            i += melhor_tamanho

    sys.stdout.write("\n".join(resultados) + "\n")

if __name__ == '__main__':
    resolver()
