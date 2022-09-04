import random
op1 = 'Pedra'
op2 = 'Papel'
op3 = 'Tesoura'
lista = [op1, op2,op3]
npc = random.choice(lista)
choice = int(input('Escolha \n 1 Pedra \n 2 Papel \n 3 Tesoura \n'))
while choice > 3 or choice < 1:
    print('Escolha Invalida')
    choice = int(input('Escolha \n 1 Pedra \n 2 Papel \n 3 Tesoura \n'))
if choice == 1:
    if npc == op1:
        print('{} X {} Empate'.format(op1,npc))
    elif npc == op2:
        print('{} X {} Voce Perdeu'.format(op1,npc))
    else:
        print('{} X {} Voce Venceu'.format(op1,npc))
elif choice == 2:
    if npc == op1:
        print('{} X {} Voce Venceu'.format(op2,npc))
    elif npc == op2:
        print('{} X {} Empate'.format(op2,npc))
    else:
        print('{} X {} Voce Perdeu'.format(op2,npc))
elif choice == 3:
    if npc == op1:
        print('{} X {} Voce Perdeu'.format(op3,npc))
    elif npc == op2:
        print('{} X {} Voce Venceu'.format(op3,npc))
    else:
        print('{} X {} Empate'.format(op3,npc) )
