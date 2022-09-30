cadastro = {}
gols = []
total = 0
cadastro['nome'] = str(input('Nome do Jogador: '))
cadastro['partidas'] = int(input(f'Quantas partidas {cadastro["nome"]} jogou: '))
for c in range(0,cadastro['partidas']):
    gols.append(int(input(f'Quantos Gols {cadastro["nome"]} fez na {c+1}° Partida: ')))
cadastro['gols'] = gols
for c in range(0,len(gols)):
    total += gols[c]
cadastro['total'] = total
print('-='*25)
print(cadastro)
print('-='*25)
for k,v in cadastro.items():
    print(f'{k} = {v}')
print('-='*25)
print(f'O Jogador {cadastro["nome"]} jogou {cadastro["partidas"]} partidas. ')
for c in range(0,len(gols)):
    print(f'=> Na Partida {c+1}, {cadastro["nome"]} fez {gols[c]} gols')
print('-='*25)