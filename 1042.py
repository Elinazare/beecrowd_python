'''Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.'''

valores = list(map(int, input().split()))

ordenados = sorted(valores)

print(ordenados[0])
print(ordenados[1])
print(ordenados[2])

print()

print(valores[0])
print(valores[1])
print(valores[2])