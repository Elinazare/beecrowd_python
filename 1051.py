salario = float(input())

if 0<=salario<=2000:
    print('Isento')
elif 2000.01<=salario<=3000:
    valor = salario-2000
    imposto = valor*0.08
    print(f'R$ {imposto:.2f}')
elif 3000.01<=salario<=4500:
    valor1= salario-2000
    valor2 = valor1 -1000
    valor3 = valor1 - valor2
    imposto = valor3*0.08 + valor2*0.18
    print(f'R$ {imposto:.2f}')
elif salario>4500: 
    valor1= salario-2000
    valor2= salario-4500
    valor3=(valor1-valor2)-1000
    valor4 = valor1 - valor2 - valor3
    imposto = valor2*0.28 + valor3*0.18 + valor4*0.08
    print(f'R$ {imposto:.2f}')

