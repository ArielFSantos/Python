class Conta_Corrente():
    def __init__(self,num_conta,nome,saldo):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def Alterar_Nome(self):
        name = input("Qual Novo Nome?: ")
        self.nome = name
    def Deposito(self):
        value = int(input("Valor do deposito: "))
        self.saldo += value
    def Saque(self):
        value = int(input("Valor Saque: "))
        self.saldo -= value
    def Saldo(self):

        if self.saldo <= 0:
            pass
        else:
            print(f"{self.saldo}")

conta = Conta_Corrente(00,'Ariel',1000)
conta.Saldo()