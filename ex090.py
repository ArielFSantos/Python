biblioteca = {}
biblioteca['nome'] = str(input('Qual seu Nome: '))
biblioteca['media'] = float(input(f'Media de {biblioteca["nome"]} : '))
if biblioteca["media"] >=7:
    biblioteca['situac'] = 'Aprovado'
else:
    biblioteca['situac'] = 'Reprovado'
print('-=' * 25)
for v,s in biblioteca.items():
    print(f'{v} = {s}')
print('-=' * 25)