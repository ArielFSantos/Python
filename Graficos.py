import matplotlib.pyplot as plt

dias = []
vest = []
transp = []
aliment = []

quantdias = int(input('Quantos dias: '))

for c in range(1,quantdias+1):

    dias.append(c)
    aux = int(input(f'Gasto dia {c} Com Alimentação: '))
    aliment.append(aux)
    aux = int(input(f'Gasto dia {c} Com Vestuario: '))
    vest.append(aux)
    aux = int(input(f'Gasto dia {c} Com Transporte: '))
    transp.append(aux)

plt.plot(dias,aliment,label='Alimentação',marker='o',markerfacecolor = 'Blue')
plt.plot(dias,vest,label='Vestuario',marker='o',markerfacecolor = 'Blue')
plt.plot(dias,transp,label='Transporte',marker='o',markerfacecolor = 'Blue')

plt.title('Gráficos de Despesas')
plt.ylabel('Despesas em R$')
plt.xlabel('Dia')
plt.legend(loc=2)
plt.show()