mes =int(input())

mes_correspondente = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if 1<=mes<=12:
    print(mes_correspondente[mes-1])
