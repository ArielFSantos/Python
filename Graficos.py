import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [100,0,0,150,0]
b = [0,40,50,0,45]
c = [0,0,100,300,50]

plt.plot(x,y,label='Alimentação',marker='o',markerfacecolor = 'Blue')
plt.plot(x,b,label='Vestuario',marker='o',markerfacecolor = 'Blue')
plt.plot(x,c,label='Transporte',marker='o',markerfacecolor = 'Blue')

plt.title('Gráficos de Despesas')
plt.ylabel('Despesas em R$')
plt.xlabel('Dia')
plt.legend(loc=2)
plt.show()
