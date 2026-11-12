n = int(input())
vogais = set("aeiouAEIOU")

for _ in range(n):
    sobrenome = input().strip()
    consoantes_seguidas = 0
    dificil = False

    for letra in sobrenome:
        if letra not in vogais:
            consoantes_seguidas += 1
            if consoantes_seguidas == 3:
                dificil = True
                break

        else:
            consoantes_seguidas = 0

    if dificil:
        print(f"{sobrenome} nao eh facil")
    else:
        print(f"{sobrenome} eh facil")