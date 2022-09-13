contage = contM = contF = sx =  0

while exit != 0:

    sx = int(input('[1] Masculino [2] Feminino : '))
    age = int(input('Digite Idade : '))


    if age > 17:
        contage+=1
    if sx == 1:
        contM+=1
    if sx == 2 and age < 20:
        contF+=1
    exit = int(input('Qualquer numero para continuar. 0 Para sair : '))
print('_'*33)
print('Total de Pessoas acima de 18 : {}\nTotal de Homens : {}\nMulheres abaixo de 20 anos : {} '.format(contage,contM,contF))
print('_'*33)
