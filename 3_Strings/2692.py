n, m = map(int, input().split())

# Dicionário para guardar as trocas nos dois sentidos
trocas = {}

for _ in range(n):
    tecla1, tecla2 = input().split()
    trocas[tecla1] = tecla2
    trocas[tecla2] = tecla1

# Cria uma tabela de tradução rápida para strings
tabela = str.maketrans(trocas)

# Lê e corrige cada uma das M frases
for _ in range(m):
    frase = input()
    print(frase.translate(tabela))