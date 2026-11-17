import sys

def resolver():
    linhas = sys.stdin.read().splitlines()
    
    for linha in linhas:
        resultado = []
        em_italico = False
        em_negrito = False
        
        for caractere in linha:
            if caractere == '_':
                if not em_italico:
                    resultado.append('<i>')
                    em_italico = True
                else:
                    resultado.append('</i>')
                    em_italico = False
            elif caractere == '*':
                if not em_negrito:
                    resultado.append('<b>')
                    em_negrito = True
                else:
                    resultado.append('</b>')
                    em_negrito = False
            else:
                resultado.append(caractere)
                
        print("".join(resultado))

if __name__ == "__main__":
    resolver()
