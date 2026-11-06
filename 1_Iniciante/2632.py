import math
import sys

def obter_raio_e_dano(magia, nivel):

    tabela = {
        "fire": (200, [20, 30, 50]),
        "water": (300, [10, 25, 40]),
        "earth": (400, [25, 55, 70]),
        "air": (100, [18, 38, 60]),
    }
    dano, raios = tabela[magia]
    return raios[nivel - 1], dano


def resolver():
    input = sys.stdin.read
    dados = input().split()

    if not dados:
        return

    T = int(dados[0])
    idx = 1

    for _ in range(T):

        w = int(dados[idx])
        h = int(dados[idx + 1])
        x0 = int(dados[idx + 2])
        y0 = int(dados[idx + 3])

        magia = dados[idx + 4]
        nivel = int(dados[idx + 5])
        cx = int(dados[idx + 6])
        cy = int(dados[idx + 7])

        idx += 8

        x_min, x_max = x0, x0 + w
        y_min, y_max = y0, y0 + h

        raio, dano = obter_raio_e_dano(magia, nivel)

        ponto_proximo_x = max(x_min, min(cx, x_max))
        ponto_proximo_y = max(y_min, min(cy, y_max))

        dist_x = cx - ponto_proximo_x
        dist_y = cy - ponto_proximo_y
        distancia_quadrada = dist_x**2 + dist_y**2

        if distancia_quadrada <= raio**2:
            print(dano)
        else:
            print(0)

if __name__ == "__main__":
    resolver()