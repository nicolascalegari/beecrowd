import sys

def main():

    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    while True:
        try:

            n_str = next(iterator)
            m_str = next(iterator)
            N = int(n_str)
            M = int(m_str)
            
            pos_player = None
            pos_pokemon = None
            
            for i in range(N):
                for j in range(M):
                    val = int(next(iterator))
                    if val == 1:
                        pos_player = (i, j)
                    elif val == 2:
                        pos_pokemon = (i, j)
            
            distancia = abs(pos_player[0] - pos_pokemon[0]) + abs(pos_player[1] - pos_pokemon[1])
            
            print(distancia)
            
        except StopIteration:

            break

if __name__ == '__main__':
    main()
