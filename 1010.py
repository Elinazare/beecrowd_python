'''Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o
código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.'''

codigo, n_peças, valor_uniario = input().split()
codigo2, n_peças2, valor_uniario2 = input().split()

n_peças,n_peças2 =  float(n_peças),float(n_peças2)
valor_uniario,valor_uniario2 =float(valor_uniario), float(valor_uniario2)

total = n_peças*valor_uniario + n_peças2*valor_uniario2

print(f'VALOR A PAGAR: R$ {total:.2f}')





