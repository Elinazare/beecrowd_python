hora_inicial, minuto_inicial, hora_final, minuto_final  = map(int, input().split())

inicial = hora_inicial*60 + minuto_inicial
final= hora_final*60 + minuto_final

if (inicial > final):
    final += 24*60

tempo_hora = (final - inicial)//60
tempo_min = (final - inicial)%60

if inicial==final:
    tempo_hora = 24
    tempo_min = 0

print(f'O JOGO DUROU {tempo_hora} HORA(S) E {tempo_min} MINUTO(S)')


