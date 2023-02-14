class TV():
    def __init__(self,canal=2,volume=31):
        self.canal = canal
        self.volume = volume

    def MudarCanal(self):
        choice = int(input('Digite o Novo canal: '))
        while choice < 1 or choice > 100:
            choice = int(input('Digite o Novo canal: '))
        self.canal = choice


    def MudarVolume(self):
        choice = int(input('Novo Volume: '))
        self.volume = choice
    def Exibir(self):
        print(self.canal,self.volume)

teve = TV(1,50)
teve.MudarCanal()
teve.MudarVolume()
teve.Exibir()