import sys

def resolver():

    leds_por_digito = {
        '1': 2, '2': 5, '3': 5, '4': 4, '5': 5,
        '6': 6, '7': 3, '8': 7, '9': 6, '0': 6
    }

    entrada = sys.stdin.read().split()
    if not entrada:
        return

    n = int(entrada[0])

    for i in range(1, n + 1):
        numero = entrada[i]
        total_leds = 0

        for digito in numero:
            total_leds += leds_por_digito[digito]

        print(f"{total_leds} leds")

if __name__ == "__main__":
    resolver()