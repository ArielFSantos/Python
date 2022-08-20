import random

a1 = str(input('Digite o Nome do 1 Aluno : '))
a2 = str(input('Digite o Nome do 2 Aluno : '))
a3 = str(input('Digite o Nome do 3 Aluno : '))

listaAlunos = [a1,a2,a3]

random.shuffle(listaAlunos)

print(listaAlunos)

