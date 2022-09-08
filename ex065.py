soma = cont = 0
num = int(input('Digite um numero inteiro : '))
menor = maior = num
while num != 0:

    cont += 1
    aux = num
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    media = soma / cont

    print('A Media dos {} Numeros Informados é : {:.0f}'.format(cont,media))
    print('O Maior numero é: {} e o menor é: {}'.format(maior,menor))

    num = int(input('[0] Para Sair ou Digite um novo numero : '))
print('Processo Finalizado')