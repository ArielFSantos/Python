from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Digite seu Nome: '))
cadastro['idade'] = int(input('Digite seu ano de nascimento '))
cadastro['clt'] = int(input('Digite o numero da Carteira [0] Se nao tem: '))
if cadastro['clt'] != 0:
    cadastro['contrato'] = int(input('Digite o Ano da Contratação: '))
    cadastro['salario'] = float(input('Digite o Salario: '))
    idade_aposent = (datetime.now().year - cadastro['idade'])+35
    ano_aposent = cadastro['contrato']+35
    print(f'Ola {cadastro["nome"]} Voce ira se aposentar com {idade_aposent} Anos, em {ano_aposent} ')
else:
    print('FIM')