listaNum = []

def group1(choice):
    return group2([],choice)

def group2(current,group):
    if group:
        return group2(current,group[1:]) + group2(current+[group[0]],group[1:])
    return [current]

while True:
    num = int(input('Digite um Numero [0 Para Sair]: '))
    if num == 0 :
        break
    listaNum.append(num)

choice = listaNum
print(group1(choice))

