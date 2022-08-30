nomeCidade = str(input('Digite o nome da Sua Cidade : '))
city = nomeCidade.split()

if city[:5].upper() == 'SANTO':
    print('Começa com Santo')
else:
    print('Não começa com Santo')