nota1, nota2, nota3, nota4 = map(float, input().split())

Media = (nota1*2 + nota2*3 + nota3*4 + nota4*1)/10

if Media>=7:
    print(f'Media: {Media:.1f}')
    print('Aluno aprovado.')
elif Media<5:
    print(f'Media: {Media:.1f}')
    print('Aluno reprovado.')
else:
    print(f'Media: {Media:.1f}')
    print('Aluno em exame.')
    nota_exame=float(input('Nota do exame: '))
    media_final=(Media + nota_exame)/2
    if nota_exame>=5:
        print('Aluno aprovado.')
        print(f'Media Final: {media_final}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media_final}')

