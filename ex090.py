biblioteca = {'aprovado':'APROVADO','reprovado':'REPROVADO'}
biblioteca['nome'] = str(input('Qual seu Nome: '))
biblioteca['media'] = float(input(f'Media de {biblioteca["nome"]} : '))
if biblioteca["media"] >=7:
    biblioteca['situac'] = 'Aprovado'
else:
    biblioteca['situac'] = 'Reprovado'
print('-=' * 25)
print(f'Ola {biblioteca["nome"]} Sua Média é {biblioteca["media"]} Voce esta {biblioteca["situac"]}')
print('-=' * 25)