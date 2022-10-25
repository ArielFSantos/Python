import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


import matplotlib.pyplot as plt
dias = []
vest = []
transp = []
aliment = []

quantdias = int(input('Quantos dias: '))

class despesas:
    def aliment():
        for c in range(0, quantdias):
            dias.append(c + 1)
            aux = int(input(f'Gasto dia {c + 1} Com Alimentação: '))
            aliment.append(aux)
    def vest():
        for c in range(0, quantdias):
            aux = int(input(f'Gasto dia {c + 1} Com Vestuario: '))
            vest.append(aux)
    def transp():
        for c in range(0, quantdias):
            aux = int(input(f'Gasto dia {c + 1} Com Transporte: '))
            transp.append(aux)

class graficos:
    def grafAliment():

        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(dias, aliment)  # perform linear regression
        Y_pred = linear_regressor.predict(aliment)
        plt.scatter(dias, Y_pred)



        plt.plot(dias,aliment,label='Alimentação',marker='o',markerfacecolor = 'Blue')
        plt.plot(dias,aliment,  c = 'g', ls='-', lw='1', marker='x', label='Predição')
        plt.title('Despesas de Alimentação')
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        plt.legend(loc=2)
        plt.show()
    def grafVest():
        plt.plot(dias,vest,label='Vestuario',marker='o',markerfacecolor = 'Blue')
        plt.title('Despesas de Vestimenta')
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        plt.legend(loc=2)
        plt.show()

    def grafTransp():
        plt.plot(dias,transp,label='Transporte',marker='o',markerfacecolor = 'Blue')
        plt.title('Despesas de Transporte')
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        plt.legend(loc=2)
        plt.show()
    def grafGeral():
        plt.plot(dias, transp, label='Transporte', marker='o', markerfacecolor='Blue')
        plt.plot(dias, vest, label='Vestuario', marker='o', markerfacecolor='Blue')
        plt.plot(dias, aliment, label='Alimentação', marker='o', markerfacecolor='Blue')
        plt.title('Grafico Despesas Gerais')
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        plt.legend(loc=2)
        plt.show()


despesas.aliment()
despesas.vest()
despesas.transp()



graficos.grafAliment()
graficos.grafVest()
graficos.grafTransp()
graficos.grafGeral()