speed = int(input('Informe a Velocidade do Veiculo : '))
if speed < 80:
    print('Velocidade Permitida')
else:
    multa=(speed-80)*7
    print('Velocidade Proibida, Voce recebera uma multa de R${:.2f} '.format(multa))