def decifrar_mensagem_oculta():

    quantidade_casos = int(input())
    
    for _ in range(quantidade_casos):
        linha = input()
        
        palavras = linha.split()
        
        letras_iniciais = [palavra[0] for palavra in palavras]
        
        mensagem_oculta = "".join(letras_iniciais)
        
        print(mensagem_oculta)

if __name__ == "__main__":
    decifrar_mensagem_oculta()