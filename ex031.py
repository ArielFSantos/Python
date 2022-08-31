range = float(input('Digite a Distancia da Viagem : '))
if range <201:
    price = range*0.5
else:
    price = range*0.45

print('Valor da Viagem de  {} KMs é de R${:.2f}'.format(range,price))
