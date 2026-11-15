import sys

def resolver():
    linhas = sys.stdin.read().splitlines()
    
    for linha in linhas:
        if not linha.strip():
            continue
            
        n = int(linha.strip())
        if n == 0:
            break
            
        x = n // 2
        y = n // 2
        
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
        
        direcao = 0
        passos_na_direcao_atual = 1
        mudancas_de_direcao = 0
        
        def imprimir_quadro(px, py):
            for r in range(n):
                linha_matriz = []
                for c in range(n):
                    if r == px and c == py:
                        linha_matriz.append('X')
                    else:
                        linha_matriz.append('O')
                print("".join(linha_matriz))
            print('@')

        imprimir_quadro(x, y)
        
        passos_dados = 1
        total_posicoes = n * n
        
        while passos_dados < total_posicoes:
            for _ in range(passos_na_direcao_atual):
                if passos_dados >= total_posicoes:
                    break

                x += dx[direcao]
                y += dy[direcao]
                passos_dados += 1
                
                imprimir_quadro(x, y)
                
            direcao = (direcao + 1) % 4
            mudancas_de_direcao += 1
            
            if mudancas_de_direcao % 2 == 0:
                passos_na_direcao_atual += 1

if __name__ == "__main__":
    resolver()