lista=[]
cont= i = 0
while True:
    lista.append(int(input('Digite um Numero : ')))
    if lista[i] == 5:
        cont += 1
    choice = str(input('Deseja Continuar ? [S/N] : '))
    while choice not in 'sSnN':
        choice = str(input('Valor Incorreto, Deseja Continuar ? [S/N] : '))
    if choice in 'nN':
         break
    i +=1
reverse=list(reversed(lista))
print('Foram Digitados {} Numeros.'.format(len(lista)))
print('Lista Decrescente : {} '.format(reverse))
if cont > 0:
    print('O Numero 5 Foi Digitado {} Vezes'.format(cont))
else:
    print('O Numero 5 Não Foi Digitado')