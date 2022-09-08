cont_maior = 0
cont_menor = 0
for c in range (0,7):
    ano = int(input('Digite o Ano de Nascimento : '))
    if (2022 - ano) >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print('Maiores : {} \nMenores : {}'.format(cont_maior,cont_menor))