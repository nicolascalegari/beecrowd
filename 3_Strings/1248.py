import sys

def main():
    entrada = sys.stdin.read().splitlines()
    if not entrada:
        return
    
    n = int(entrada[0].strip())
    
    indice_linha = 1
    for _ in range(n):
        if indice_linha >= len(entrada):
            break
        
        diet = entrada[indice_linha]
        breakfast = entrada[indice_linha+1] if indice_linha+1 < len(entrada) else ""
        lunch = entrada[indice_linha+2] if indice_linha+2 < len(entrada) else ""
        indice_linha += 3
        
        diet_counts = {}
        for char in diet:
            diet_counts[char] = diet_counts.get(char, 0) + 1
            
        cheater = False
        
        for char in (breakfast + lunch):
            if char in diet_counts and diet_counts[char] > 0:
                diet_counts[char] -= 1
            else:
                cheater = True
                break
                
        if cheater:
            print("CHEATER")
        else:
            remaining = []
            for char, count in diet_counts.items():
                remaining.extend([char] * count)
            
            remaining.sort()
            print("".join(remaining))

if __name__ == '__main__':
    main()