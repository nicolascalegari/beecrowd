S, P, N = map(int, input().split())

salgados_restantes = S - (N * P)

if salgados_restantes >= P:
    print("SIM")
else:
    print("NAO")