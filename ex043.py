peso = float(input('Digite seu peso : '))
altura = float(input('Digite Sua Altura : '))
imc = peso / (altura*altura)

if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 26 and imc > 18.4:
    print('Peso Ideal')
elif imc < 31 and imc > 24:
    print('Sobrepeso')
elif imc < 41 and imc > 29:
    print('Obesidade')
else:
    print('Obesidade Morbida')