import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    linha = input()

    num1 = int(linha[2:4])
    num2 = int(linha[5:8])
    num3 = int(linha[11:13])

    print(num1 + num2 + num3)