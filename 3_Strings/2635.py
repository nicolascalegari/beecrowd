import sys

def resolver():

    dados = sys.stdin.read().split()
    if not dados:
        return
    
    indice = 0
    total_dados = len(dados)
    
    while indice < total_dados:
        n = int(dados[indice])
        indice += 1
        
        # Lê as N palavras já pesquisadas
        historico = dados[indice : indice + n]
        indice += n
        
        q = int(dados[indice])
        indice += 1
        
        # Processa cada uma das Q consultas
        for _ in range(q):
            consulta = dados[indice]
            indice += 1
            
            quantidade = 0
            maior_tamanho = 0
            
            for palavra in historico:
                if palavra.startswith(consulta):
                    quantidade += 1
                    tamanho_atual = len(palavra)
                    if tamanho_atual > maior_tamanho:
                        maior_tamanho = tamanho_atual
            
            if quantidade == 0:
                print("-1")
            else:
                print(f"{quantidade} {maior_tamanho}")

if __name__ == "__main__":
    resolver()
