saldo=1000
limite_saque = 3
extrato = ""
usuarios = []

def op_saque(saldo,limite_saque,extrato):
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
            while value > saldo:
                print(20 * '=-')
                value = int(input('Valor Muito Alto, Digite Valor menor: R$ '))
                saldo -= value

    else:
        print('Limite de Saque Excedido')


def op_deposito(extrato,saldo,/):
    value = int(input('Digite o Valor do Deposito: R$ '))
    extrato += f'\nDeposito: R${value}'
    while value < 1:
        print('Valor Invalido!"')
        value = int(input('Digite o Valor do Deposito: R$ '))
    saldo += value


def op_extrato():
    print('-=-=-=-=-=-= EXTRATO =-=-=-=-=-=-')
    print(extrato)
    print('Saldo Atual da Conta: R$ ', saldo)



def op_novo_usuario(usuarios):
    list_aux = []
    list_aux.append(str(input('Digite o Seu Nome: ')))
    list_aux.append(str(input('Digite o Seu Endereço: ')))
    aux = int(input('Digite Seu CPF: '))
    for cpf in usuarios:
        while cpf == aux:
            print('O CPF ja esta em uso')
            aux = int(input('Digite Seu CPF: '))
    list_aux.append(aux)
    usuarios.append(list_aux)

while True:
    print(20 * '=-')
    print('[1] Saque '
          '\n[2] Deposito '
          '\n[3] Extrato '
          '\n[4] Nova Conta '
          '\n[5] Listar Contas'
          '\n[6] Novo Usuário'
          '\n[7] Sair ')
    choice = int(input("Qual Operação Deseja Realizar?: "))
    print(20 * '=-')
    while choice < 1 or choice > 7:
        print('Escolha Invalida!"')
        print('[1] Saque '
              '\n[2] Deposito '
              '\n[3] Extrato '
              '\n[4] Nova Conta '
              '\n[5] Listar Contas'
              '\n[6] Novo Usuário'
              '\n[7] Sair ')
        choice = int(input("Qual Operação Deseja Realizar?: "))
        print(20 * '=-')
    if choice == 1:
        op_saque(saldo=saldo,limite_saque=limite_saque,extrato=extrato)
    elif choice == 2:
        op_deposito(extrato,saldo)
    elif choice == 3:
        op_extrato()

    elif choice == 6:
        op_novo_usuario(usuarios)
    elif choice == 7:
        if extrato == "":
            print('Não Foram Realizadas Movimentações')
        print('Saldo Atual da Conta: R$ ', saldo)
        print(usuarios)
        print('Obrigado, Tenha um Bom dia <3')
        break

