def fatorial(num):
    calc = fat = num
    while calc > 2:
        calc = calc - 1
        fat = fat * calc
        print(f'{num} x ', end='')
        num -= 1
    print('2 x 1 : ',fat)
    return f'O Valor do Fatorial de {num} é {fat}'


print(fatorial(5))