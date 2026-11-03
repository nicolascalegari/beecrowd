import sys

def main():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        angulo_hora = int(input_data[idx])
        angulo_minuto = int(input_data[idx+1])
        idx += 2
        
        horas = angulo_hora // 30
        minutos = angulo_minuto // 6
        
        print(f"{horas:02d}:{minutos:02d}")

if __name__ == '__main__':
    main()
