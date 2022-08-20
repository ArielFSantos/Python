import random
aluno1=input('Digite o Nome do Aluno 1 : ')
aluno2=input('Digite o Nome do Aluno 2 : ')
aluno3=input('Digite o Nome do Aluno 3 : ')
aluno4=input('Digite o Nome do Aluno 4 : ')

lista=[aluno1,aluno2,aluno3,aluno4]

escolha = random.choice(lista)

print(escolha)
