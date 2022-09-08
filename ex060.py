
num = int(input('Digite um Numero : '))
fat = num

while num != 1:
    num = num - 1
    fat = fat*num
print('O Fatorial de : {} é : {}'.format(num,fat))


