import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    a = int(entrada[0])
    b = int(entrada[1])

    abs_b = abs(b)

    r = a % abs(b)
    q = (a - r) // b

    print(f"{q} {r}")

if __name__ == '__main__':
    main()