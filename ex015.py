km = int(input('Quantos KMs foram andados com este carro? '))
dias = int(input('Quantos dias voce ficou com o carro? '))
print('Valor total a Ser Pago R${}'.format((km*0.15)+(dias*60)))
if 0 == km:
    print('Teste')
