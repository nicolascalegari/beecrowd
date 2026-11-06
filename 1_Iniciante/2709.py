import sys

def eh_primo(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def resolver():

    linhas = sys.stdin.read().split()
    if not linhas:
        return

    idx = 0
    while idx < len(linhas):

        M = int(linhas[idx])
        idx += 1

        moedas = []
        for _ in range(M):
            moedas.append(int(linhas[idx]))
            idx += 1

        N = int(linhas[idx])
        idx += 1

        soma = 0
        for i in range(M - 1, -1, -N):
            soma += moedas[i]

        if eh_primo(soma):
            print(
                "You’re a coastal aircraft, Robbie, a large silver aircraft."
            )
        else:
            print("Bad boy! I’ll hit you.")


if __name__ == "__main__":
    resolver()
