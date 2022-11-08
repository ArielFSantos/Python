import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dias = []
vest = []
transp = []
aliment = []

class Graficos:
    def __init__(self,despesa,nome):
        self.despesa = despesa
        self.nome = nome

    def GerarGrafico(self):
        x = np.array(dias).reshape(-1, 1)
        reg = LinearRegression().fit(x, self.despesa)
        a_coeff = reg.coef_
        l_coeff = reg.intercept_
        plt.plot(dias, l_coeff + a_coeff * dias, label='Regressão', color='red')
        plt.plot(dias, self.despesa, label=f'{self.nome}', marker='o',markerfacecolor='Blue')
        plt.title(f'Despesas de {self.nome}')
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        plt.legend(loc=2)
        plt.show()
    @staticmethod
    def GraficoGeral():
        plt.plot(dias, aliment, label='Alimentação', marker='o')
        plt.plot(dias, vest, label='Vestimenta', marker='o')
        plt.plot(dias, transp, label='Transporte', marker='o')
        plt.title('Gráfico de Despesas')
        plt.ylabel('Despesa em R$')
        plt.xlabel('Dia')
        plt.legend()
        plt.show()

while True:
    dias.append(int(input('Qual o dia? ')))
    aliment.append(float(input('Valor Gasto em Alimentação: R$')))
    vest.append(float(input('Valor Gasto em Vestuário: R$')))
    transp.append(float(input('Valor Gasto em Transporte: R$')))
    while True:
        choice = str(input('Deseja? continuar? [S/N] ')).strip().upper()[0]
        if choice in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if choice == 'N':
        break

sorted(dias)
despesa1 = Graficos(vest,'Vestimenta')
despesa2 = Graficos(transp,'Transporte')
despesa3 = Graficos(aliment,'Alimentação')
despesa1.GerarGrafico()
despesa2.GerarGrafico()
despesa3.GerarGrafico()
Graficos.GraficoGeral()





















