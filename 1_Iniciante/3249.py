def resolver():
    n = int(input())
    vitorias = 0
    
    for _ in range(n):
        batalha = input().strip()
        # Se a sequência "CD" NÃO estiver presente, o herói venceu
        if "CD" not in batalha:
            vitorias += 1
            
    print(vitorias)

if __name__ == "__main__":
    resolver()