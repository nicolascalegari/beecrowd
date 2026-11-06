import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    total_len = len(input_data)

    while idx < total_len:
        n = int(input_data[idx])
        idx += 1

        trabalhos = [int(x) for x in input_data[idx : idx + n]]
        idx += n

        soma_total = sum(trabalhos)
        soma_rangel = 0
        menor_diferenca = float('inf')

        for t in trabalhos:
            soma_rangel += t
            soma_gugu = soma_total - soma_rangel
            diferenca = abs(soma_rangel -soma_gugu)

            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
            else:
                break

        print(menor_diferenca)

if __name__ == "__main__":
    main()