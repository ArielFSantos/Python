lista = []
par = []
impar = []

while True :

  lista.append(int(input('Digite um Numero : ')))

  choice = str(input('Deseja continuar? [S/N] : '))
  while choice not in 'sSnN':
   choice = str(input('Valor Invalido, Deseja continuar? [S/N] : '))
  if choice in 'nN':
    break

for c in range(0,len(lista)):
  if lista[c] % 2 == 0:
    par.append(lista[c])
  else:
   impar.append(lista[c])

print('Lista Total : ',lista)
print('Lista Par : ',par)
print('Lista Impar : ',impar)
