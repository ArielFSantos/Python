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