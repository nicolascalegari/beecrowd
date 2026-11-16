import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    while True:
        try:
            n_str = next(iterator)
            N = int(n_str)
        except StopIteration:
            break
        
        teto = [int(next(iterator)) for _ in range(N)]
            
        chao = [int(next(iterator)) for _ in range(N)]
            

        def simular(inicio_no_teto):
            current_side = 0 if inicio_no_teto else 1
            switches = 0
            
            if current_side == 0 and teto[0] == 0:
                return float('inf')
            if current_side == 1 and chao[0] == 0:
                return float('inf')
                
            for i in range(N - 1):
                if current_side == 0:  
                    if teto[i+1] != 0 and teto[i+1] <= teto[i]:
                        continue
                    else:
                        current_side = 1
                        switches += 1
                        if chao[i+1] != 0 and chao[i+1] <= chao[i]:
                            continue
                        else:
                            return float('inf')
                else:
                    if chao[i+1] != 0 and chao[i+1] <= chao[i]:
                        continue
                    else:
                        current_side = 0
                        switches += 1
                        if teto[i+1] != 0 and teto[i+1] <= teto[i]:
                            continue
                        else:
                            return float('inf')
            return switches

        opcoes_teto = simular(inicio_no_teto=True)
        opcoes_chao = simular(inicio_no_teto=False)
        
        print(min(opcoes_teto, opcoes_chao))

if __name__ == '__main__':
    solve()
