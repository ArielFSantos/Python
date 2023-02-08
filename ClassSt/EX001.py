class Bola():
    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ = circ
        self.material = material

    def Trocar(self):
        choice = input("Digite a Nova Cor: ")
        self.cor = choice

    def Mostrar(self):
        print(f"A Cor é {self.cor} ")



bola1 = Bola(cor='azul',circ=50,material='Borracha')

bola1.Trocar()
bola1.Mostrar()