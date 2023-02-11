class Retangulo:
    def __init__(self,LadoA=0,LadoB=0):
        self.LadoA = LadoA
        self.LadoB = LadoB

    def Perguntar(self):

        self.LadoA = input("Lado A:")
        self.LadoB = input("Lado B:")

    def Mudar(self):

        choice = input("Mudar Lado A ou B: ")
        value = input("Novo Valor: ")

        if choice in "Aa":
            self.LadoA = value
        if choice in "Bb":
            self.LadoB = value
    def Exibir(self):
        print(f"Lado A: {self.LadoA} Lado B: {self.LadoB}")


retangulo = Retangulo()
retangulo.Perguntar()
retangulo.Exibir()