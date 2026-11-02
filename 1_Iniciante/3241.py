def resolver():
    n = int(input())

    for _ in range(n):
        expressao = input().strip()

        if expressao == "P=NP":
            print("skipped")
        else:
            a, b = expressao.split('+')
            resultado = int(a) + int(b)
            print(resultado)

if __name__ == "__main__":
    resolver()