import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    estrelas = [int(x) for x in data[1:n+1]]
    
    estrelas_atacadas = [0] * n
    
    i = 0
    while 0 <= i < n:
        estrelas_atacadas[i] = 1
        
        carneiros_atuais = estrelas[i]
        
        if estrelas[i] > 0:
            estrelas[i] -= 1
            
        if carneiros_atuais % 2 != 0:
            i += 1
        else:
            i -= 1

    total_estrelas_atacadas = sum(estrelas_atacadas)
    total_carneiros_restantes = sum(estrelas)
    
    print(f"{total_estrelas_atacadas} {total_carneiros_restantes}")

if __name__ == "__main__":
    main()