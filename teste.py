import matplotlib.pyplot as plt
x = []
despesas = []

dias = int(input('Quantos dias: '))

for c in range (0,dias):
    x.append(c+1)
    despesas.append(input('Digite o Valor :'))

y=despesas[:]

plt.title('Gráfico de Despesas')
plt.ylabel('Despesas')
plt.xlabel('Mês')
plt.axis(ymin=0)
plt.plot(x,y)
plt.legend(loc=2)
plt.show()


