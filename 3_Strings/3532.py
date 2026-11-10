n = int(input())

vogais = {'a','e','i','o','u'}

for _ in range(n):
    palavra = input().strip()

    if palavra[-1] in vogais:
        print(palavra + 'h')
    else:
        print(palavra)