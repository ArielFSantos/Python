from matplotlib import pyplot as plt
from faker import Faker
from random import randint

fk = Faker()
with  open("dados.txt",'w') as arquivo:
    for c in range(0, 4):
        aux = str(randint)
        arquivo.write(str(randint(0,10)))

