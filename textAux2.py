import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dias = [1,2,3,4,5]
vest = [4,5,6,7,8]
transp = [6,2,3,8,9]
aliment = []


class Graficos:
    def __init__(self, despesa, nome):
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

        plt.plot(dias, self.despesa, label=f'{self.nome}', marker='o', markerfacecolor='Blue')
        plt.title(f'Despesas de {self.nome}')
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        plt.legend(loc=2)


    @staticmethod
    def GraficoGeral():

        plt.title('Gráfico de Despesas')
        plt.ylabel('Despesa em R$')
        plt.xlabel('Dia')
        plt.legend()
        plt.show()




sorted(dias)
despesa1 = Graficos(vest, 'Vestimenta')
despesa2 = Graficos(transp, 'Transporte')

despesa1.Regressao()
despesa2.Regressao()


