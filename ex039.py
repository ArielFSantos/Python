ano = int(input('Informe o ano que voce nasceu : '))
idade = 2022 - ano
if idade < 18:
    print('Ainda vai se alistar daqui {} Ano(s)'.format(18-idade))
elif idade > 18:
    print('Esta Atrasado {} Ano(s) para se alistar'.format(idade-18))
else:
    print('Esta na hora de alistar vc tem {} anos '.format(idade))