import random
from time import sleep
jogo=[]
num = int(input('Quantos sorteios de jogos? : '))
print('-='*20)
for c in range (0,num):
    for a in range (0,6):
        jogo.append(random.randint(1,61))
    sleep(1)
    print(f'Jogo Numero {c+1}: {jogo}')
    jogo.clear()
print('-='*20)