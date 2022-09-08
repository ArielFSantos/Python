idadeauxM=0
contF=0
old=0
media = 0
for c in range (1,5):

    sx = int(input('{}º Pessoa, Digite 1 para Homen e 2 para Mulher : '.format(c)))

    idade = int(input('{}º Pessoa, Digite sua idade : '.format(c)))
    media += idade
    nome = str(input('{}º Pessoa, Digite seu nome'.format(c)))

    if sx == 1:
        if idade > idadeauxM:
            old = nome
            idadeauxM = idade
    if sx == 2:
        if idade < 20:
            contF+=1


media = media/4
print('Media de Idade : {}'.format(media))
print('Homen Mais Velho : {}'.format(old))
print('Mulheres Com Menos de 20 : {}'.format(contF))