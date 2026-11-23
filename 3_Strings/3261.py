def resolver():

    try:
        original = input().strip()
        infectada = input().strip()
    except EOFError:
        return

    tam_orig = len(original)
    tam_inf = len(infectada)

    inicio = 0
    while inicio < tam_orig and inicio < tam_inf and original[inicio] == infectada[inicio]:
        inicio += 1

    fim_orig = tam_orig - 1
    fim_inf = tam_inf - 1

    while fim_orig >= inicio and fim_inf >= inicio and original[fim_orig] == infectada[fim_inf]:
        fim_orig -= 1
        fim_inf -= 1

    comprimento_inserido = max(0, fim_inf - inicio + 1)

    print(comprimento_inserido)

if __name__ == '__main__':
    resolver()