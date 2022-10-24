import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [2,5,6,7,8,1,0]
b = [1,2,3,4,5,6,7]
c = [7,8,6,5,4,1,2]

plt.plot(x,y,label='teste1')
plt.plot(b,c,label='teste2')

plt.title('Graficos Teste')
plt.legend(loc=2)
plt.show()

