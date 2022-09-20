lista = []
dados = []
while True:
    dados.append(str(input('Digite Seu Nome : ')))
    dados.append(float(input('Digite Seu Peso : ')))
    if len(lista) == 0 :
        maior = menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()

    choice = str(input('Deseja Continuar? [S/N] : '))
    while choice not in "sSnN":
        choice = str(input('Dado Invalido, Deseja Continuar? [S/N] : '))
    if choice in 'nN':
        break


print(lista)
print('Foram Cadastradas {} pessoas '.format(len(lista)))
print('Maior Peso : {}KG'.format(maior))
print('Menor Peso : {}KG'.format(menor))