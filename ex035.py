l1 = int(input('Informe o Valor do 1° Lado : '))
l2 = int(input('Informe o Valor do 2° Lado : '))
l3 = int(input('Informe o Valor do 3° Lado : '))

if (l1 + l2) > l3 and (l1 + l3 ) > l2 and (l2 + l3 ) > l1:
    print('As medidas {},{},{} formam um Triangulo'.format(l1,l2,l3))
else:
    print('As Medidas {},{},{} Não Formam um Triangulo'.format(l1,l2,l3))
