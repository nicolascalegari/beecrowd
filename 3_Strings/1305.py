import sys

def resolver_arredondamento():

    linhas = sys.stdin.read().splitlines()
    
    indice = 0
    while indice < len(linhas):

        linha_num = linhas[indice].strip()
        if not linha_num:
            indice += 1
            continue
            
        if indice + 1 >= len(linhas):
            break
            
        linha_corte = linhas[indice + 1].strip()
        indice += 2
        
        if '.' in linha_num:
            parte_inteira_str, parte_frac_str = linha_num.split('.')
        else:
            parte_inteira_str = linha_num
            parte_frac_str = ""
            
        if not parte_inteira_str:
            valor_inteiro = 0
        else:
            valor_inteiro = int(parte_inteira_str)
            
        _, corte_frac_str = linha_corte.split('.')
        
        tamanho_maximo = max(len(parte_frac_str), len(corte_frac_str))
        frac_num_normalizada = parte_frac_str.ljust(tamanho_maximo, '0')
        frac_corte_normalizada = corte_frac_str.ljust(tamanho_maximo, '0')
        
        if frac_num_normalizada > frac_corte_normalizada:
            valor_inteiro += 1
            
        print(valor_inteiro)

if __name__ == '__main__':
    resolver_arredondamento()
