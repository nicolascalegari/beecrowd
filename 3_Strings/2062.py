n = int(input())

palavras = input().split()

corrigidas = []

for p in palavras:
    if len(p) == 3 and p.startswith("OB"):
        corrigidas.append("OBI")
    elif len(p) == 3 and p.startswith("UR"):
        corrigidas.append("URI")
    else:
        corrigidas.append(p)

print(" ".join(corrigidas))