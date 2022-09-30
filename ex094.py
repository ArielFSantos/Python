cadastro = []
mulheres = []
biblioteca = {}
quantidade = idade = somaIdade = 0
while True:
    nome = str(input('Nome: '))
    cadastro.append(nome)

    sx = str(input('Sexo [F/M]: '))
    while sx not in 'mMfF':
        sx = str(input('Valor Invalido Somente [F/M]: '))
    cadastro.append(sx)

    if sx in 'fF':
        mulheres.append(nome)
    idade = int(input('Idade: '))
    somaIdade += idade
    cadastro.append(idade)

    biblioteca = cadastro


    choice = str(input('Deseja Continuar? [S/N]: '))
    while choice not in 'nNsS':
        choice = choice = str(input('Valor Invalido, somente [S/N]: '))

    quantidade += 1

    if choice in 'nN':
        break

media = somaIdade/quantidade

print(biblioteca)
print('-='*30)
print(f'A) Ao Todo Foram {quantidade} pessoas Cadastradas')
print(f'B) A Media de idade é de {media} anos.')
print(f'C) As Mulheres Cadastradas Foram {mulheres}')
print(f'D) Lista de Pessoas Acima da Media: ')

print('-='*30)
