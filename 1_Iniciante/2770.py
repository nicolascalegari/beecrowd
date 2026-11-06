import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    total_len = len(input_data)

    while idx < total_len:
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        m = int(input_data[idx + 2])
        idx += 3

        emp_min, emp_max = (x, y) if x < y else (y, x)

        saida = []

        for _ in range(m):
            xi = int(input_data[idx])
            yi = int(input_data[idx + 1])
            idx += 2

            cli_min, cli_max = (xi, yi) if xi < yi else (yi, xi)

            if cli_min <= emp_min and cli_max <= emp_max:
                saida.append("Sim")
            else:
                saida.append("Nao")

        print('\n'.join(saida))

if __name__ == '__main__':
    main()