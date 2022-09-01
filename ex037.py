num = int(input('Digite um Numero Inteiro : '))
choice = int(input('Escolha uma das Bases para Conversão \n 1 Binario \n 2 Octal \n 3 Hexadecimal \n'))
while choice > 3 or choice < 1:
    choice = int(input('Escolha uma das Bases para Conversão \n 1 Binario \n 2 Octal \n 3 Hexadecimal \n'))
if choice == 1:
    print('{} Convertido para BINARIO é igual a : {}'.format(num,bin(num)[2:]))
elif choice == 2:
    print('{} Convertido para OCTAL é igual a : {}'.format(num, oct(num)[2:]))
else:
    print('{} Convertido para HEXADECIMAL é igual a : {}'.format(num, hex(num)[2:]))