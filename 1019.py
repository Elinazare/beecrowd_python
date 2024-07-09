segundos = int(input())

lista = [3600,60,1]
tempo = []

for valor in lista:
    tempo.append(segundos//valor)
    segundos %=valor

print(f'{tempo[0]}:{tempo[1]}:{tempo[2]}')
    
    