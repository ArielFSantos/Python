n1 = int(input('Digite o 1° Valor : '))
n2 = int(input('Digite o 2° Valor : '))

if n1 > n2:
    print('O Numero {} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('O Numero {} é maior que {}'.format(n2, n1))
else:
    print('Os Numeros {} e {} São Iguais'.format(n1,n2))