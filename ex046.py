from time import sleep

num = int(input('Digite Inicio da Contagem Regressiva : '))

for c in range (num,0,-1):
    sleep(1)
    print(c)