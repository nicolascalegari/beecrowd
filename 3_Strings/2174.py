n = int(input())

pomekons_unicos = set()

for _ in range(n):
    nome = input().strip()
    pomekons_unicos.add(nome)

faltam = 151 - len(pomekons_unicos)

print(f"Falta(m) {faltam} pomekon(s).")