import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dias = [1,2,3,4,5]
vest = [4,5,8,6,10]
transp = [6,2,3,8,9]
aliment = [2,4,6,1,2]

class Graficos:
    def __init__(self,despesa,nome):
        self.despesa = despesa
        self.nome = nome

    def Regressao(self):
        x = np.array(dias).reshape(-1, 1)
        reg = LinearRegression().fit(x, self.despesa)
        a_coeff = reg.coef_
        l_coeff = reg.intercept_
        plt.plot(dias, l_coeff + a_coeff * dias, label='Regressão', color='red')
        Graficos.GerarGrafico(self)
    def GerarGrafico(self):

        plt.plot(dias, self.despesa, label=f'{self.nome}', marker='o',markerfacecolor='Blue')
        plt.title(f'Despesas de {self.nome}')
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        plt.legend(loc=2)
        plt.show()
    def GraficoGeral(self):
        plt.plot(dias, aliment, label='Alimentação', marker='o')
        plt.plot(dias, vest, label='Vestimenta', marker='o')
        plt.plot(dias, transp, label='Transporte', marker='o')
        plt.title('Gráfico de Despesas')
        plt.ylabel('Despesa em R$')
        plt.xlabel('Dia')
        plt.legend()
        plt.show()


despesa1 = Graficos(vest,'Vestimenta')
despesa2 = Graficos(transp,'Transporte')
despesa3 = Graficos(aliment,'Alimentação')
despesa1.Regressao()




























