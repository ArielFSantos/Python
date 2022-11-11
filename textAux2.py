from matplotlib import pyplot as plt
from faker import Faker
from random import randint

nome = []
pont = []

fk = Faker()

for c in range(0, 4):
    nome.append(fk.name())
    pont.append(randint(0,10))

pont.hist()
plt.show()





despesa1 = Graficos(vest,'Vestimenta')
despesa2 = Graficos(transp,'Transporte')
despesa3 = Graficos(aliment,'Alimentação')

despesa1.GerarGrafico()
despesa2.GerarGrafico()
despesa3.GerarGrafico()

Graficos.GraficoGeral(dias)

despesa1.GerarGrafico()
despesa2.GerarGrafico()
despesa3.GerarGrafico()

