'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor 
pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo
fornecido. Não esqueça de imprimir o fim de linha após cada linha,'''

num = int(input())

valor_original = num

notas = [100,50,20,10,5,2,1]

qtde_notas = []

for nota in notas:
    qtde_notas.append(num//nota)
    num %=nota

print(valor_original)
for i in range(len(notas)):
    print(f'{qtde_notas[i]} nota(s) de R$ {notas[i]},00')
