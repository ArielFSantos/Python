lista=[]
while True:
    num = int(input('Digite um Numero : '))
    if num in lista:
        print('Numero Repetido!.')
    else:
        lista.append(num)
    choice = str(input('Deseja continuar? [S/N]: '))
    while choice not in 'nNsS':
        choice = str(input('Valor Invalido, Deseja continuar? [S/N]: '))
    if choice in 'Nn':
          break
listaOrd = sorted(lista)
print(listaOrd)