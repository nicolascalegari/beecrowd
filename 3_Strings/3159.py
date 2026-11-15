import sys

def resolver():
    mapeamento = {
        'a': (2, '2'), 'b': (2, '22'), 'c': (2, '222'),
        'd': (3, '3'), 'e': (3, '33'), 'f': (3, '333'),
        'g': (4, '4'), 'h': (4, '44'), 'i': (4, '444'),
        'j': (5, '5'), 'k': (5, '55'), 'l': (5, '555'),
        'm': (6, '6'), 'n': (6, '66'), 'o': (6, '666'),
        'p': (7, '7'), 'q': (7, '77'), 'r': (7, '777'), 's': (7, '7777'),
        't': (8, '8'), 'u': (8, '88'), 'v': (8, '888'),
        'w': (9, '9'), 'x': (9, '99'), 'y': (9, '999'), 'z': (9, '9999'),
        ' ': (0, '0')
    }
    
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return
    
    n = int(linhas[0])
    
    for i in range(1, n + 1):
        frase = linhas[i]
        resultado = []
        tecla_anterior = None
        
        for char in frase:
            char_lower = char.lower()
            if char_lower in mapeamento:
                tecla, sequencia = mapeamento[char_lower]
                e_maiuscula = char.isupper()
                
                # Se a tecla atual for igual à anterior e a letra NÃO for maiúscula,
                # precisamos do '*' para separar o tempo de digitação.
                if tecla == tecla_anterior and not e_maiuscula:
                    resultado.append('*')
                
                # Se for maiúscula, adicionamos o '#' antes da sequência
                if e_maiuscula:
                    resultado.append('#')
                    
                resultado.append(sequencia)
                tecla_anterior = tecla
                
        print("".join(resultado))

if __name__ == "__main__":
    resolver()
