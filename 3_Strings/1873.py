import sys

def resolver():
    regras = {
        "tesoura": ["papel", "lagarto"],
        "papel": ["pedra", "spock"],
        "pedra": ["lagarto", "tesoura"],
        "lagarto": ["spock", "papel"],
        "spock": ["tesoura", "pedra"]
    }
    
    entrada = sys.stdin.read().splitlines()
    if not entrada:
        return
        
    c = int(entrada[0].strip())
    
    for i in range(1, c + 1):
        if i >= len(entrada):
            break
            
        partes = entrada[i].split()
        if len(partes) < 2:
            continue
            
        rajesh = partes[0].lower()
        sheldon = partes[1].lower()
        
        # Caso 1: Escolhas iguais resultam em empate
        if rajesh == sheldon:
            print("empate")
        # Caso 2: A escolha de Rajesh ganha da escolha de Sheldon
        elif sheldon in regras[rajesh]:
            print("rajesh")
        # Caso 3: Sheldon ganha
        else:
            print("sheldon")

if __name__ == "__main__":
    resolver()