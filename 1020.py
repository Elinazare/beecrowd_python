'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias'''

idade_dias = int(input())

lista =[365,30,1]
idade = []

for dia in lista:
    idade.append(idade_dias//dia)
    idade_dias %= dia
    
print(f'{idade[0]} ano(s)\n{idade[1]} mes(es)\n{idade[2]} dia(s)')