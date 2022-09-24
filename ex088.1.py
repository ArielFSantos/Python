import random
cont=0
jogo = []
num = int(input('Quantos sorteios de jogos? : '))
for c in range (0,num):
    while True :
        num = random.randint(1,61)
        if num not in jogo:
            jogo.append(num)
            cont+=1
        if cont == 6:
            break
        print(jogo)