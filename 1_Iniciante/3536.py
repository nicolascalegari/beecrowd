N = int(input())

itens = {
    "arco": 0,
    "escudo": 0,
    "espada": 0,
    "pocao": 0
}

for _ in range(N):
    item = input().strip()
    if item in itens:
        itens[item] += 1

for nome_item, quantidade in itens.items():
    print(f"{nome_item} {quantidade}")