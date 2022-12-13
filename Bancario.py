saldo = 1000
limite_saque = 3
extrato = ""
while True:
    print(20 * '=-')
    print('[1] Saque \n[2] Deposito \n[3] Extrato \n[4] Sair ')
    choice = int(input("Qual Operação Deseja Realizar?: "))
    print(20 * '=-')
    while choice < 1 or choice > 4:
        print('Escolha Invalida!"')
        print('[1] Saque \n[2] Deposito \n[3] Extrato \n[4] Sair ')
        choice = int(input("Qual Operação Deseja Realizar?: "))
        print(20 * '=-')
    if choice == 1:
        if limite_saque != 0:
            limite_saque -= 1
            value = int(input('Qual Valor Deseja Sacar?: R$ '))
            while value > 500 or value < 1:
                print(20 * '=-')
                value = int(input('Valor Invalido!" \nQual Valor Deseja Sacar?: R$ '))
            if value > 0 and value < 501:
                if saldo > value:
                    extrato += f'\nSaque: R${value}'
                    saldo -= value
                else:
                    print(20 * '=-')
                    value = int(input('Valor Muito Alto, Digite Valor menor ou [0] para sair: R$ '))
                    if value == 0:
                        break
                    saldo -= value
        else:
            print('Limite de Saque Excedido')
    if choice == 2:
        extrato += f'\nDeposito: R${value}'
        value = int(input('Digite o Valor do Deposito: R$ '))
        while value < 1:
            print('Valor Invalido!"')
            value = int(input('Digite o Valor do Deposito: R$ '))
        saldo += value
    if choice == 3:
        print('-=-=-=-=-=-= EXTRATO =-=-=-=-=-=-')
        print(extrato)
        print('Saldo Atual da Conta: R$ ', saldo)
    if choice == 4:
        if extrato == "":
            print('Não Foram Realizadas Movimentações')
        print('Saldo Atual da Conta: R$ ', saldo)
        print('Obrigado, Tenha um Bom dia <3')
        break

