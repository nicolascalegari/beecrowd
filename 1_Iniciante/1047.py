h_inicio, m_inicio, h_fim, m_fim = map(int, input().split())

inicio_total_minutos = h_inicio * 60 + m_inicio
fim_total_minutos = h_fim * 60 + m_fim
duracao_minutos = fim_total_minutos - inicio_total_minutos

if duracao_minutos <= 0:
    duracao_minutos += 24 * 60

duracao_horas = duracao_minutos // 60
duracao_minutos_restantes = duracao_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos_restantes} MINUTO(S)")