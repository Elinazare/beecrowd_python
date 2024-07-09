codigo, qtde = map(int, input().split())

lista = [codigo, qtde]

if codigo==1:
    total = qtde*4
    print(f'Total: R$ {total:.2f}')
elif codigo==2:
    total = qtde*4.5
    print(f'Total: R$ {total:.2f}')
elif codigo==3:
    total = qtde*5
    print(f'Total: R$ {total:.2f}')
elif codigo==4:
    total = qtde*2
    print(f'Total: R$ {total:.2f}')
else:
    total = qtde*1.5
    print(f'Total: R$ {total:.2f}')
