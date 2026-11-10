import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    for item in input_data:
        n = int(item)

        for asteriscos in range(1, n + 1, 2):
            espacos = (n - asteriscos) // 2
            print(" " * espacos + "*" * asteriscos)

        espacos_tronco1 = (n - 1) // 2
        print(" " * espacos_tronco1 + "*")

        espacos_tronco2 = (n - 3) // 2
        print(" " * espacos_tronco2 + "***")

        print()

if __name__ == '__main__':
    main()