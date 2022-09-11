soma = cont = 0
while True:
    num = int(input('Digite um Numero Inteiro : '))

    if num == 999:
        break

    cont += 1
    soma+=num

print('{} numeros foram somados, valor total : {} '.format(cont,soma))
