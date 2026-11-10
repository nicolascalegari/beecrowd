import sys

def solve():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    iterator = iter(input_lines)
    
    try:
        N_str = next(iterator)
        while not N_str.strip():
            N_str = next(iterator)
        N = int(N_str)
    except StopIteration:
        return

    fragments = []
    
    # Leitura dos fragmentos
    for _ in range(N):
        filename = next(iterator).strip()
        while not filename:
            filename = next(iterator).strip()
            
        frag_lines = []
        while True:
            line = next(iterator)
            if line.strip() == "***END***":
                break
            # Normalização da linha
            cleaned = ' '.join(line.split())
            if cleaned:  # Se não for vazia
                frag_lines.append(cleaned)
        
        fragments.append((filename, frag_lines))

    # Leitura do trecho de código alvo
    target_lines = []
    while True:
        try:
            line = next(iterator)
            if line.strip() == "***END***":
                break
            cleaned = ' '.join(line.split())
            if cleaned:
                target_lines.append(cleaned)
        except StopIteration:
            break

    # Mapeia cada linha do alvo para seus índices correspondentes
    target_map = {}
    for idx, line in enumerate(target_lines):
        target_map.setdefault(line, []).append(idx)

    global_max_len = 0
    matching_files = []

    # Comparação de cada fragmento com o alvo
    for filename, frag_lines in fragments:
        max_frag_match = 0
        current_matches = {}  # Mapeia indice_no_alvo -> comprimento da sequência atual
        
        for line in frag_lines:
            next_matches = {}
            if line in target_map:
                for t_idx in target_map[line]:
                    # Se a linha anterior do alvo (t_idx - 1) fazia parte de uma sequência ativa
                    length = current_matches.get(t_idx - 1, 0) + 1
                    next_matches[t_idx] = length
                    if length > max_frag_match:
                        max_frag_match = length
            current_matches = next_matches

        # Atualiza o recorde global e a lista de arquivos correspondentes
        if max_frag_match > global_max_len:
            global_max_len = max_frag_match
            matching_files = [filename]
        elif max_frag_match == global_max_len and global_max_len > 0:
            matching_files.append(filename)

    if global_max_len == 0:
        print(0)
    else:
        print(f"{global_max_len} {' '.join(matching_files)}")

if __name__ == "__main__":
    solve()
