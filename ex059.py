res = 0
num1 = int(input('Digite o 1° numero: '))
num2 = int(input('Digite o 2° numero: '))
op = int(input('Selecione Operação Desejada \n[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NUMEROS \n[5]SAIR DO PROGRAMA\n'))
while op != 5:
    if op==1:
        res = num1+num2
        print('A Soma é : {} '.format(res))
    elif op==2:
        res = num1*num2
        print('A Multiplicação é : {} '.format(res))
    elif op==3:
        if num1>num2:
            res = num1
        else:
            res = num2
        print('Maior Numero: {}'.format(res))
    elif op==4:
        num1 = int(input('Informe primeiro valor novamente : '))
        num2 = int(input('Informe primeiro valor novamente : '))
    op = int(input('Selecione Operação Desejada \n[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NUMEROS \n[5]SAIR DO PROGRAMA\n'))

print('Operações Finalizadas')
