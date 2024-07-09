dia1 = int(input().split()[1])
hora,minuto,segundo = map(int, input().split(" : "))

dia2 = int(input().split()[1])
hora2,minuto2,segundo2 = map(int, input().split(" : "))

tempo = segundo + minuto*60 + hora*3600 + dia1*24*3600
tempo2 = segundo2 + minuto2*60 + hora2*3600 + dia2*24*3600

dif = tempo2 - tempo

dias = dif//(24*3600)
dif = dif%(24*3600)

horas = dif//3600
dif = dif%3600

minutos = dif//60
segundos = dif%60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')