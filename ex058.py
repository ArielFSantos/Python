import random
num = random.randint(0,10)

choice = int(input('Digite um Numero de 1 a 10 : '))

while choice != num:
    print('Erooooouu, tente novamente!"')
    choice = int(input('Digite um Numero de 1 a 10 : '))

print('Acertoooou, é o numero {} '.format(num))