from matplotlib import pyplot as plt
from faker import Faker
from random import randint

nomes = []
pont = []
fk = Faker()

with open("dados.txt",'w') as arquivo:
    for c in range(0, 100):
        arquivo.write(fk.name() + str(randint(0,11)) +'\n')


with open("dados.txt",'r') as arquivo:
    for v in arquivo:
        nomes.append(v[:-2])
        pont.append(int(v[-2]))


plt.hist(pont, label='Histograma das Pontuações')
plt.ylabel('Pontuações')
plt.xlabel('Probabilidades')
plt.grid('5')

plt.show()
