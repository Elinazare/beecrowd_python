A,B,C = map(float, input().split())

lados  = [A,B,C]
lados.sort(reverse=True)

A, B, C = lados 

if A>=B+C:
    print('NÃO FORMA TRIANGULO')
else:
    if A**2 ==B**2 + C**2:
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')   
    if A==B==C:
        print('TRIANGULO EQUILATERO')   
    if A==B or B==C or A==C:
        print('TRIANGULO ISOSCELES')
        
        