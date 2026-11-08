h_paulo, m_paulo = map(int, input().split())
tempo_paulo = h_paulo * 60 + m_paulo

limite_horario = 7 * 60

grupo_leva_fumo = False

for _ in range(3):
    h, m = map(int, input().split())
    tempo_bolsita = h * 60 + m

    atrasado = tempo_bolsita > limite_horario
    flagrado = tempo_bolsita >= tempo_paulo

    if atrasado and flagrado:
        grupo_leva_fumo = True

if grupo_leva_fumo:
    print("FUMO")
else:
    print("LIVRE")