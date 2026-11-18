import sys

def contar_aliteracoes():
    for linha in sys.stdin:
        linha = linha.strip()
        if not linha:
            continue
        
        palavras = linha.split()
        
        total_aliteracoes = 0
        em_aliteracao = False
        
        for i in range(len(palavras) - 1):
            letra_atual = palavras[i][0].lower()
            proxima_letra = palavras[i + 1][0].lower()
            
            if letra_atual == proxima_letra:
                # Se uma nova sequência de aliteração começou
                if not em_aliteracao:
                    total_aliteracoes += 1
                    em_aliteracao = True
            else:
                # A sequência de letras iguais foi interrompida
                em_aliteracao = False
                
        print(total_aliteracoes)

if __name__ == "__main__":
    contar_aliteracoes()