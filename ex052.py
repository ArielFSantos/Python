num = int(input('Digite Numero : '))
cont = 0
for c in range (num,0,-1):
    if num % c == 0:
        cont +=1
if cont == 2:
    print('O Numero {} é Primo'.format(num))
else:
    print('O Numero {} não é primo'.format(num))