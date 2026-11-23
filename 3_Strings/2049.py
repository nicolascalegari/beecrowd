import sys

def resolver():

    linhas = sys.stdin.read().splitlines()
    
    indice = 0
    instancia = 1
    primeiro_caso = True
    
    while indice < len(linhas):
        assinatura = linhas[indice].strip()
        
        if not assinatura:
            indice += 1
            continue
            
        if assinatura == "0":
            break
            
        painel = linhas[indice + 1].strip()
        
        if not primeiro_caso:
            print()
        primeiro_caso = False
        
        print(f"Instancia {instancia}")
        if assinatura in painel:
            print("verdadeira")
        else:
            print("falsa")
            
        instancia += 1
        indice += 2

if __name__ == "__main__":
    resolver()
