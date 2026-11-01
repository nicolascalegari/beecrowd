import sys

def main():
    linhas = sys.stdin.read().splitlines()

    if len(linhas) < 3:
        return

    A = linhas[0]
    B = linhas[1]
    C = linhas[2]

    print(f"{A}{B}{C}")
    print(f"{B}{C}{A}")
    print(f"{C}{A}{B}")

    print(f"{A[:10]}{B[:10]}{C[:10]}")

if __name__ == '__main__':
    main()