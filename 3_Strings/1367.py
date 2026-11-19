import sys

def resolver():

    input_data = sys.stdin.read().splitlines()

    linha_idx = 0
    while linha_idx < len(input_data):
        linha = input_data[linha_idx].strip()
        if not input_data or linha == "":
            linha_idx += 1
            continue

        n = int(linha)
        if n == 0:
            break

        linha_idx += 1

        erros = {}
        acertos = {}

        for _ in range(n):
            partes = input_data[linha_idx].split()
            problema = partes[0]
            tempo = int(partes[1])
            julgamento = partes[2]
            linha_idx += 1

            if julgamento == "correct":
                acertos[problema] = tempo
            else:
                erros[problema] = erros.get(problema, 0) + 1

        total_corretos = 0
        tempo_total = 0

        for problema, tempo in acertos.items():
            total_corretos += 1
            tempo_total += tempo + (erros.get(problema, 0) * 20)

        print(f"{total_corretos} {tempo_total}")

if __name__ == "__main__":
    resolver()