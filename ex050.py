soma=0
cont=0
for c in range (0,6):
    cont = cont+1
    num = int(input('Digite o {} Numero Inteiro : '.format(cont)))
    if num % 2 == 0:
        soma += num

print('Soma Pares :{} '.format(soma))