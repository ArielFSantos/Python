import matplotlib.pyplot as plt
c=0
dias = []
aliment = []
vest = []
transp = []

quantdias = int(input('Quantos dias: '))

for c in range(c,quantdias):

    dias.append(c+1)
    aux = int(input(f'Gasto dia {c+1} Com Alimentação: '))
    aliment.append(aux)
    aux = int(input(f'Gasto dia {c+1} Com Vestuario: '))
    vest.append(aux)
    aux = int(input(f'Gasto dia {c+1} Com Transporte: '))
    transp.append(aux)

plt.plot(dias,aliment,label='Alimentação',marker='o',markerfacecolor = 'Blue')
plt.plot(dias,vest,label='Vestuario',marker='o',markerfacecolor = 'Blue')
plt.plot(dias,transp,label='Transporte',marker='o',markerfacecolor = 'Blue')

plt.title('Gráficos de Despesas')
plt.ylabel('Despesas em R$')
plt.xlabel('Dia')
plt.legend(loc=2)
plt.show()



