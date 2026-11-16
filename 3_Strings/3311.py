import sys

def main():
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    while True:
        try:
            linha_n = next(iterator).strip()
            if not linha_n:
                continue
            N = int(linha_n)
        except StopIteration:
            break
        
        nomes = []
        for _ in range(N):
            nomes.append(next(iterator).strip())
            
        nomes.sort(key=lambda nome: nome[0])
        
        for nome in nomes:
            print(nome)

if __name__ == '__main__':
    main()