import sys

nomes = [linha.rstrip('\r\n') for linha in sys.stdin if linha.strip()]

if nomes:
    ultima_crianca = max(nomes, key=str.lower)
    print(ultima_crianca)