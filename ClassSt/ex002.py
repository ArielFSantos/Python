class Quadrado():
    def __init__(self,size1,size2):
        self.recovery = None
        self.recovery2 = None
        self.size1 = size1
        self.size2 = size2
    def Mudar(self):
        self.recovery = self.size1
        self.recovery2 = self.size2
        choice = int(input('Lado 1 ou Lado 2: '))

        if choice == 1:
            value = int(input('Novo Valor: '))
            self.size1 = value
        if choice == 2:
            value = int(input('Novo Valor: '))
            self.size2 = value

    def Retornar(self):
        self.size1 = self.recovery
        self.size2 = self.recovery2

    def Calcular(self):
        area = self.size1 * self.size2
        print(f'O Valor da Area é : {area}')

quad = Quadrado(size1=3,size2=5)
quad.Calcular()
quad.Mudar()
quad.Calcular()
quad.Retornar()
quad.Calcular()
