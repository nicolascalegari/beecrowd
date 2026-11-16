import sys

def main():
    input_data = sys.stdin.read().splitlines()

    for n in input_data:
        n = n.strip()
        if not n:
            continue

        if "13" in n:
            print(f"{n} es de Mala Suerte")
        else:
            print(f"{n} NO es de Mala Suerte")

if __name__ == '__main__':
    main()