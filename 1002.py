'''A fórmula para calcular a área de uma circunferência é: area = π . raio2.
π = 3.14159:
- Efetue o cálculo da área.
Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal'''


raio = float(input())
area = 3.14159*(raio**2)

print(f'A={area:.4f}')