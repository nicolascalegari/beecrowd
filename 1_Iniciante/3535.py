import sys

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    Q = int(input_data[1])

    A = [int(x) for x in input_data[2:2+N]]

    # Construção do vetor de somas acumuladas (Prefix Sum)
    # prefix_sum[i] guardará a soma de goiabinhas do pacote 1 até o pacote i
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    # Processamento das Q perguntas
    idx = 2 + N
    output = []
    for _ in range(Q):
        L = int(input_data[idx])
        R = int(input_data[idx + 1])
        idx += 2
        
        # A soma no intervalo [L, R]
        total_intervalo = prefix_sum[R] - prefix_sum[L - 1]
        output.append(str(total_intervalo))

    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
