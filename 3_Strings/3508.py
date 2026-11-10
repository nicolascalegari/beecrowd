import sys

def solve():
    input_data = sys. stdin.read().splitlines()
    if not input_data:
        return

    lines = [line.strip() for line in input_data if line.strip()]

    if len(lines) >= 2:
        S = lines[0]
        T = lines[1]

        if S > T:
            print(S)
        else:
            print(T)

if __name__ == '__main__':
    solve()