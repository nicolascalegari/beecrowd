import sys

def main():
    entrada = sys.stdin.read().splitlines()
    if not entrada:
        return
    
    n = int(entrada[0].strip())
    
    for i in range(1, n + 1):
        if i >= len(entrada):
            break
            
        palavra = entrada[i].strip()
        
        if len(palavra) == 5:
            print(3)
        else:
            matches_one = 0
            if palavra[0] == 'o': matches_one += 1
            if palavra[1] == 'n': matches_one += 1
            if palavra[2] == 'e': matches_one += 1
            
            if matches_one >= 2:
                print(1)
            else:
                print(2)

if __name__ == '__main__':
    main()