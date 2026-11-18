import sys

def encontrar_faixas_de_letras():

    for linha in sys.stdin:

        linha = linha.replace("\n", "")
        
        # Filtra apenas as letras minúsculas (ignora espaços) e remove duplicatas usando set()
        letras_unicas = sorted(list(set([caractere for caractere in linha if 'a' <= caractere <= 'z'])))
        
        # Se não houver letras válidas, imprime apenas uma linha vazia
        if not letras_unicas:
            print()
            continue
            
        faixas = []
        inicio_faixa = letras_unicas[0]
        letra_anterior = letras_unicas[0]
        
        # Percorre as letras a partir da segunda para agrupar as consecutivas
        for i in range(1, len(letras_unicas)):
            letra_atual = letras_unicas[i]
            
            # Verifica se a letra atual é consecutiva à anterior na tabela ASCII
            if ord(letra_atual) == ord(letra_anterior) + 1:
                letra_anterior = letra_atual
            else:
                # Se quebrou a sequência, fecha a faixa anterior e inicia uma nova
                faixas.append(f"{inicio_faixa}:{letra_anterior}")
                inicio_faixa = letra_atual
                letra_anterior = letra_atual
                
        # Adiciona a última faixa que ficou pendente após o término do loop
        faixas.append(f"{inicio_faixa}:{letra_anterior}")
        
        print(", ".join(faixas))

if __name__ == "__main__":
    encontrar_faixas_de_letras()
