import sys

def resolver():

    for linha in sys.stdin:

        texto = linha.rstrip('\n')
        
        texto = texto.replace(" ,", ",").replace(" .", ".")
        
        print(texto)

if __name__ == '__main__':
    resolver()