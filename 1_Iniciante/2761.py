import sys
import struct

def main():

    for linha in sys.stdin:
        if not linha.strip():
            continue
        
        partes = linha.split(maxsplit=3)
        if len(partes) < 4:
            continue
            
        inteiro = int(partes[0])
        float_original = float(partes[1])
        caracter = partes[2]
        frase = partes[3].rstrip('\r\n')
        
        float_simples = struct.unpack('f', struct.pack('f', float_original))[0]
        
        # 1ª Saída: Tudo junto, sem espaços
        print(f"{inteiro}{float_simples:.6f}{caracter}{frase}")
        
        # 2ª Saída: Separados por tabulação (\t)
        print(f"{inteiro}\t{float_simples:.6f}\t{caracter}\t{frase}")
        
        # 3ª Saída: Com largura de 10 caracteres, todos alinhados à direita (:>10)
        print(f"{inteiro:10d}{float_simples:10.6f}{caracter:>10s}{frase:>10s}")

if __name__ == '__main__':
    main()
