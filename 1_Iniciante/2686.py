import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    for item in input_data:
        m = float(item)

        if (m >= 0 and m < 90) or m == 360:
            print("Bom Dia!!")
        elif m >= 90 and m < 180:
            print("Boa Tarde!!")
        elif m >= 180 and m < 270:
            print("Boa Noite!!")
        elif m >= 270 and m < 360:
            print("De Madrugada!!")

        segundos_totais = int(m * 240) + 21600

        segundos_totais %= 86400

        horas = segundos_totais // 3600
        resto = segundos_totais % 3600
        minutos = resto // 60
        segundos = resto % 60

        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

if __name__ == '__main__':
    main()