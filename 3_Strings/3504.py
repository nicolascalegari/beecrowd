import sys

def resolver():

    linhas = sys.stdin.read().splitlines()
    
    for frase in linhas:

        if not frase and frase != "":
            continue
            
        frase_invertida = frase[::-1]
        
        if frase == frase_invertida:
            print(f"A frase [{frase}] eh palindrome")
        else:
            print(f"A frase [{frase}] nao eh palindrome")

if __name__ == "__main__":
    resolver()
