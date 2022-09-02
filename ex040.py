n1 = int(input('Digite a 1° Nota : '))
n2 = int(input('Digite a 2° Nota : '))

media = (n1 + n2)/2

if media < 5:
    print('Media {:.2f} Voce esta Reprovado '.format(media))
elif media >=7:
    print('Media {:.2f} Voce esta Aprovado '.format(media))
else:
    print('Media de {:.2f} Voce Esta de Recuperação'.format(media))
