saldo = 1000
limite_saque = 3
extrato = ""
usuarios = []
contas = []
numero_conta = 0


def op_saque(saldo,limite_saque,extrato):

    if limite_saque != 0:
        limite_saque -= 1
        value = int(input('Qual Valor Deseja Sacar?: R$ '))
        while value > 500 or value < 1:
            print(20 * '=-')
            value = int(input('Valor Invalido!" \nQual Valor Deseja Sacar?: R$ '))
        while value > saldo:
            print(20 * '=-')
            value = int(input('Valor Muito Alto, Digite Valor menor: R$ '))
        saldo -= value
        extrato += f'\nSaque: R${value}'
    else:
        print('Limite de Saque Excedido')
    return saldo,limite_saque,extrato

def op_deposito(extrato,saldo):
    value = int(input('Digite o Valor do Deposito: R$ '))
    while value < 1:
        print('Valor Invalido!"')
        value = int(input('Digite o Valor do Deposito: R$ '))
    saldo += value
    extrato += f'\nDeposito: R${value}'
    return extrato,saldo


def op_extrato(extrato, saldo):
    print('-=-=-=-=-=-= EXTRATO =-=-=-=-=-=-')
    print(extrato)
    print('Saldo Atual da Conta: R$', saldo)


def op_novo_usuario(usuarios):
    list_aux = []
    list_aux.append(str(input('Digite o Seu Nome: ')))
    list_aux.append(str(input('Digite o Seu Endereço: ')))
    aux = int(input('Digite Seu CPF: '))
    for cpf in usuarios:
        while cpf[2] == aux:
            print('O CPF ja esta em uso')
            aux = int(input('Digite Seu CPF: '))
    list_aux.append(aux)
    usuarios.append(list_aux)


def op_nova_conta(contas,numero_conta):
    numero_conta += 1
    list_aux = []
    list_aux.append('001')
    list_aux.append(numero_conta)
    cont = 0
    for user in usuarios:
        cont += 1
        print(cont, user[0])
    aux = int(input('Selecione o usuario: '))
    aux = usuarios[aux - 1][0]
    list_aux.append(aux)
    contas.append(list_aux)
    print(contas)
    return numero_conta


def op_lista(contas, usuarios):
    choice = int(input('[1] Listar Contas'
                       '\n[2] Listar Usuarios '
                       '\nOperação: '))

    while choice != 1 and choice != 2:
        print('Escolha Invalida!"')
        choice = int(input('[1] Listar Contas'
                           '\n[2] Listar Usuarios'
                           '\nOperação: '))
    if choice == 1:
        for cont in contas:
            print(cont)
    else:
        for user in usuarios:
            print(user)


def op_saida():
    if extrato == "":
        print('Não Foram Realizadas Movimentações')
    print('Saldo Atual da Conta: R$ ', saldo)
    print('Obrigado, Tenha um Bom dia <3')



while True:
    print(20 * '=-')
    print('[1] Saque '
          '\n[2] Deposito '
          '\n[3] Extrato '
          '\n[4] Adicionar '
          '\n[5] Listar'
          '\n[0] Sair ')
    choice = int(input("Qual Operação Deseja Realizar?: "))
    print(20 * '=-')
    while choice < 0 or choice > 7:
        print('Escolha Invalida!"')
        print('[1] Saque '
              '\n[2] Deposito '
              '\n[3] Extrato '
              '\n[4] Adicionar '
              '\n[5] Listar'
              '\n[0] Sair ')
        choice = int(input("Qual Operação Deseja Realizar?: "))
        print(20 * '=-')

    if choice == 1:
        saldo, limite_saque, extrato = op_saque(saldo=saldo,limite_saque=limite_saque,extrato=extrato)
    elif choice == 2:
        extrato, saldo = op_deposito(extrato,saldo)
    elif choice == 3:
        op_extrato(extrato, saldo)
    elif choice == 4:
        while True:
            choice = int(input('[1] Nova Conta '
                               '\n[2] Novo Usuario'
                               '\n[0] Sair'
                               '\nOperação : '))
            if choice == 2:
                op_novo_usuario(usuarios)
            if choice == 1:
                op_nova_conta(contas)
            if choice == 0:
                break
    elif choice == 5:
        op_lista(contas, usuarios)

    elif choice == 6:
        op_novo_usuario(usuarios)
    elif choice == 0:
        op_saida()
        break


