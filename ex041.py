ano = int(input('Informe o Ano de Nascimento : '))
idade = 2022-ano

if idade < 10:
    print('Voce tem {} Anos. Categoria Mirim'.format(idade))
elif idade > 9 and idade < 15:
    print('Voce tem {} Anos. Categoria Infantil'.format(idade))
elif idade > 14 and idade < 20:
    print('Voce tem {} Anos. Categoria Junior'.format(idade))
elif idade > 19 and idade < 26:
    print('Voce tem {} Anos. Categoria Senior'.format(idade))
else:
    print('Voce tem {} Anos. Categoria Master'.format(idade))