import sys

def main():

    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])

    regioes = 1 + (n * (n - 1)) // 2 + (n * (n - 1) * (n - 2) * (n - 3)) // 24

    print(regioes)

if __name__ == '__main__':
    main()