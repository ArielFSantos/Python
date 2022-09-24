lista = []
cont=0
while True:
    cont +=1
    nome = str(input('Digite o seu Nome : '))
    nota1 = float(input('Digite Primeira Nota : '))
    nota2 = float(input('Digite Segunda Nota : '))
    media = (nota1 + nota2) / 2
    lista.append([nome,nota1,nota2,media])
    choice = str(input('Deseja Continuar? [S/N] : '))
    
    if choice in 'Nn':
        break

print('=-' * 30)
for c in range(0,len(nome)):
    print(f'{c+1} Aluno. Nome : {lista[c][0]} Notas {lista[c][1]} e {lista[0][2]} Media {lista[c][3]}')

print('=-' * 30)

for c in range(0,len(nome)):
    print(f'{c+1} Aluno = {lista[c][0]}')

aluno = int(input('Gostaria de Saber a Nota de Qual Aluno?'))
