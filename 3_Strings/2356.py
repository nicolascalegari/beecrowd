while True:
    try:
        # Lê o DNA da bactéria (D) e o código de resistência (S)
        dna = input().strip()
        resistencia = input().strip()
        
        # Verifica se a sequência S está contida no DNA D
        if resistencia in dna:
            print("Resistente")
        else:
            print("Nao resistente")
            
    except EOFError:
        # Encerra o loop quando não houver mais entradas (fim de arquivo)
        break
