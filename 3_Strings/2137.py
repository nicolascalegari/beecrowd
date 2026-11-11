import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()
        if not line:
            idx += 1
            continue

        n = int(line)
        idx += 1

        codigos = []
        for _ in range(n):
            if idx < len(lines):
                codigos.append(lines[idx].strip())
                idx += 1

        codigos.sort()

        for codigo in codigos:
            print(codigo)

if __name__ == '__main__':
    main()