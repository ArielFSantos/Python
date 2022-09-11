import random
cont=0
while True:
    play = random.randint(1, 11)
    choice = int(input('[1]Par ou [2]Impar : '))

    while choice < 1 or choice > 2:
        choice = int(input('Valor Incorreto [1]Par ou [2]Impar : '))

    num = int(input('Escolha Valor 1 a 10 : '))

    result = play+num

    if choice == 1:

        if result % 2 == 0:
            print('[{}] é Par Ganhou'.format(result))
            cont+=1
        else:
            print('[{}] é Impar Perdeu'.format(result))
            break
    else:

        if result % 2 == 0:
            print('[{}] é Par Perdeu'.format(result))
            break
        else:
            print('[{}] é Impar Ganhou'.format(result))
            cont += 1
if cont == 1:
    print('Voce Venceu 1 Vez! ')
elif cont > 1:
    print('Parabens Voce Venceu [{}] Vezes Consecutivas!'.format(cont))
else:
    print('Voce não Ganhou Nenhuma Vez')
