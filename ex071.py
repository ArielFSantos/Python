print('='*30)
print('{:^30}'.format('BANCO ARI'))
print('='*30)

valor = int(input('Valor do Saque : R$'))

cinq = valor // 50
print('{} Notas de R$50,00'.format(cinq))
vinte = (valor - (cinq * 50)) // 20
print('{} Notas de R$20,00'.format(vinte))
dez = (valor - ((cinq * 50) + (vinte * 20))) // 10
print('{} Notas de R$10,00'.format(dez))
um = (valor - ((cinq*50)+(vinte*20)+(dez*10))) // 1
print('{} Notas de R$1,00'.format(um))

