
num = int(input('Digite um Numero de 0 a 9999 : '))
while num > 9999 or num<0:
    print('Numero Invalido')
    num = int(input('Digite um Numero de 0 a 9999 : '))
else:
    if num < 10000:
    num=str(num)
    frac=num.split()

    print('Unidade : ',num[3])
    print('Dezena : ',num[2])
    print('Centena : ',num[1])
    print('Milhar : ',num[0])