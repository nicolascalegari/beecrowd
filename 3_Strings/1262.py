import sys
import math

def main():
    entrada = sys.stdin.read().splitlines()
    if not entrada:
        return
    
    iterator = iter(entrada)
    
    while True:
        try:
            rastro = next(iterator).strip()
            p_str = next(iterator).strip()
            P = int(p_str)
            
            ciclos_totais = 0
            r_count = 0
            
            for char in rastro:
                if char == 'W':
                    if r_count > 0:
                        ciclos_totais += math.ceil(r_count / P)
                        r_count = 0
                    ciclos_totais += 1
                elif char == 'R':
                    r_count += 1
            
            if r_count > 0:
                ciclos_totais += math.ceil(r_count / P)
                
            print(ciclos_totais)
            
        except StopIteration:
            break

if __name__ == '__main__':
    main()