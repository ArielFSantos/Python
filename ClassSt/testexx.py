class Quadrado():
    def __init__(self, size1, size2):
        self.size1 = size1
        self.size2 = size2

    def Mudar(self):

        choice = int(input('Lado 1 ou Lado 2: '))

        if choice == 1:
            value = int(input('Novo Valor: '))
            self.size1 = value
            self.recovery = self.size1
        if choice == 2:
            value = int(input('Novo Valor: '))
            self.size2 = value
            self.recovery = self.size2

    def Retornar(self):

        choice = int(input('Lado 1 ou Lado 2: '))

        if choice == 1:
            value = int(input('Novo Valor: '))
            self.size1 = value
        if choice == 2:
            value = int(input('Novo Valor: '))
            self.size2 = value

    def pergunta(self):

    def Calcular(self):
        area = self.size1 * self.size2
        print(f'O Valor da Area é : {area}')


quad = Quadrado(size1=5, size2=5)
quad.Calcular()
quad.Mudar()
quad.Calcular()

