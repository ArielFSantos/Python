import matplotlib.pyplot as plt
x = []
y = []


dias = int(input('Quantos dias: '))
for c in range (0,dias):
    x.append(c+1)
    y.append(input('Digite o Valor :'))



plt.title('Gráfico de Despesas')
plt.ylabel('Despesas')
plt.xlabel('Mês')
plt.plot(x,y)
plt.legend(loc=2)
plt.show()


