valor = float(input('Digite o Valor do Produto : '))
choice = int(input('Forma de Pagamento \n 1 Dinheiro/Chegue \n 2 A Vista Cartão \n 3 2x no cartão \n 4 3x ou mais no cartao \n'))

while choice < 1 or choice > 4:
    print('Opção Incorreta, Digite Novamente.')
    choice = int(input('Forma de Pagamento \n 1 Dinheiro/Chegue \n 2 A Vista Cartão \n 3 2x no cartão \n 4 3x ou mais no cartao \n'))

    if choice == 1:
        valor = valor - (valor*0.10)
        print('Valor Com Desconto de 10% R${:.2f}'.format(valor))
    elif choice == 2:
        valor = valor - (valor*0.05)
        print(('Valor Com Desconto de 5% R${:.2f}'.format(valor)))
    elif choice == 3:
        print('Valor Normal R${:.2f}'.format(valor))
    elif choice ==4:
        valor = valor + (valor*0.20)
        print('Valor Com Acrescimo de 20% {:.2f}'.format(valor))
