while True:
    try:
        palavra = input()
        n = len(palavra)
        corrigida = palavra

        for tamanho in range(n // 2, 0, -1):
            fim = palavra[n - tamanho:]
            antes_do_fim = palavra[n - 2 * tamanho : n - tamanho]

            if fim == antes_do_fim:
                corrigida = palavra[:n - tamanho]
                break

        print(corrigida)

    except EOFError:
        break