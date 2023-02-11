class Pessoa():
    def __init__(self,nome="random",idade="00",peso="00",altura="00"):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhecer(self):

        age = int(input('Quanto Deseja Envelhacer: '))
        self.idade += age
        if age <= 21:
            self.altura += 0.5*age

    def Engordar(self):
        weight = int(input('Quanto Deseja Engordar?: '))
        self.peso += weight

    def Emagrecer(self):
        weight = int(input('Quanto Deseja Emagrecer?:  '))
        self.peso -= weight
    def Crescer(self):
        size = int(input('Quanto Deseja Crescer?: '))
        self.altura += size

    def Exibir(self):
        print("nome:",self.nome," idade:",self.idade," peso:",self.peso," altura:",self.altura)

pessoa = Pessoa("Ariel",18,80,176)
pessoa.Crescer()
pessoa.Exibir()