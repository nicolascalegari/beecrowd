import sys

def main():

    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        if n == 0:
            break
            
        presentes = [int(x) for x in input_data[idx : idx + (2 * n)]]
        idx += (2 * n)
        
        maior_par = float('-inf')
        menor_par = float('inf')
        
        for i in range(n):
            soma_par = presentes[i] + presentes[(2 * n) - 1 - i]
            
            if soma_par > maior_par:
                maior_par = soma_par
            if soma_par < menor_par:
                menor_par = soma_par
                
        print(f"{maior_par} {menor_par}")

if __name__ == "__main__":
    main()
