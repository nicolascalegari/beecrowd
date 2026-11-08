import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    
    casas = []
    pai_de = [0] * (n + 1)
    cap_restante = [0] * (n + 1)
    
    idx = 1
    for i in range(1, n + 1):
        p = int(data[idx])
        r = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        casas.append({'id': i, 'pai': p, 'demanda': r, 'capacidade': c})
        pai_de[i] = p
        cap_restante[i] = c

    # Ordena as casas pela menor demanda de energia
    casas.sort(key=lambda x: x['demanda'])
    
    atendidas = 0
    
    for casa in casas:
        u = casa['id']
        d = casa['demanda']
        pode_atender = True
        
        # Verifica o caminho até a raiz (0)
        atual = u
        while atual != 0:
            if cap_restante[atual] < d:
                pode_atender = False
                break
            atual = pai_de[atual]
            
        # Se for possível, subtrai a capacidade das arestas do caminho
        if pode_atender:
            atendidas += 1
            atual = u
            while atual != 0:
                cap_restante[atual] -= d
                atual = pai_de[atual]
                
    print(atendidas)

if __name__ == '__main__':
    solve()
