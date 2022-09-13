total = contM  = 0
min = 9999999
nameMin =''
while True :
    name = str(input('Nome do Produto : '))
    price = float(input('Valor do Produto : '))

    total += price

    if price > 1000:
        contM+=1

    if price < min :

        min = price
        nameMin = name

    exit = int(input('Digite 0 para Sair : '))
    if  exit == 0:
        break
print('Total Gasto : {} \nAcima de R$1.000 : {} \nProduto Mais Barato : R${:.2f} {}'.format(total,contM,min,nameMin))