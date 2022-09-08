cont = 0
soma = 0
num = int(input('Digite um Numero Inteiro : '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um Numero Inteiro : '))
print('Numeros inseridos: {} Soma Numeros: {}'.format(cont,soma))
