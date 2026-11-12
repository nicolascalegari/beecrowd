c = int(input())

for _ in range(c):
    ataque = input().strip()
    parte1, parte2 = ataque.split('k')
    qtd_a1 = parte1.count('a')
    qtd_a2 = parte2.count('a')
    print('k' + 'a' * qtd_a1 * qtd_a2)