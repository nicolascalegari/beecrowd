import sys

def main():
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        m = int(parts[0])
        n = int(parts[1])

        if m == 0 and n == 0:
            break

        soma = m + n

        resultado_sem_zero = str(soma).replace('0','')

        print(resultado_sem_zero)

if __name__ == '__main__':
    main()