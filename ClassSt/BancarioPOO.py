class Bancario():

    def __init__(self,saldo=1000,limite_saque=3,extrato="",usuarios=[],contas=[],numero_conta=0):
        self.saldo = saldo
        self.limite_saque = limite_saque
        self.extrato = extrato
        self.usuarios = usuarios
        self.contas = contas
        self.numero_conta = numero_conta


    def start(self):
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
    def op_saque(self):

        if self.limite_saque != 0:
            self.limite_saque -= 1
            value = int(input('Qual Valor Deseja Sacar?: R$ '))
            while value > 500 or value < 1:
                print(20 * '=-')
                value = int(input('Valor Invalido!" \nQual Valor Deseja Sacar?: R$ '))
            while value > self.saldo:
                print(20 * '=-')
                value = int(input('Valor Muito Alto, Digite Valor menor: R$ '))
            self.saldo -= value
            self.extrato += f'\nSaque: R${value}'
        else:
            print('Limite de Saque Excedido')
        return self.saldo,self.limite_saque,self.extrato

    def op_deposito(self):
        value = int(input('Digite o Valor do Deposito: R$ '))
        while value < 1:
            print('Valor Invalido!"')
            value = int(input('Digite o Valor do Deposito: R$ '))
        self.saldo += value
        self.extrato += f'\nDeposito: R${value}'
        return self.extrato,self.saldo


    def op_extrato(self):
        print('-=-=-=-=-=-= EXTRATO =-=-=-=-=-=-')
        print(self.extrato)
        print('Saldo Atual da Conta: R$', self.saldo)


    def op_novo_usuario(self):
        list_aux = []
        list_aux.append(str(input('Digite o Seu Nome: ')))
        list_aux.append(str(input('Digite o Seu Endereço: ')))
        aux = int(input('Digite Seu CPF: '))
        for cpf in self.usuarios:
            while cpf[2] == aux:
                print('O CPF ja esta em uso')
                aux = int(input('Digite Seu CPF: '))
        list_aux.append(aux)
        self.usuarios.append(list_aux)


    def op_nova_conta(self):
        self.numero_conta += 1
        list_aux = []
        list_aux.append('001')
        list_aux.append(self.numero_conta)
        cont = 0
        for user in self.usuarios:
            cont += 1
            print(cont, user[0])
        aux = int(input('Selecione o usuario: '))
        aux = self.usuarios[aux - 1][0]
        self.list_aux.append(aux)
        self.contas.append(list_aux)
        print(self.contas)
        return self.numero_conta


    def op_lista(self):
        choice = int(input('[1] Listar Contas'
                           '\n[2] Listar Usuarios '
                           '\nOperação: '))

        while choice != 1 and choice != 2:
            print('Escolha Invalida!"')
            choice = int(input('[1] Listar Contas'
                               '\n[2] Listar Usuarios'
                               '\nOperação: '))
        if choice == 1:
            for cont in self.contas:
                print(cont)
        else:
            for user in self.usuarios:
                print(user)


    def op_saida(self):
        if self.extrato == "":
            print('Não Foram Realizadas Movimentações')
        print('Saldo Atual da Conta: R$ ', self.saldo)
        print('Obrigado, Tenha um Bom dia <3')





conta1 = Bancario()
conta1.start()