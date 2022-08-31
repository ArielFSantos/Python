year = int(input('Informe o Ano : '))
if year % 4 == 0:
    print('O ano de {} é Bissexto'.format(year))
else:
    print('O ano de {} não é Bissexto'.format(year))
