n1 = int(input('Digite um Numero : '))
n2 = int(input('Digite outro Numero : '))
n3 = int(input('Digite outro Numero : '))

if n1 > n2 and n3:
    maior = n1
if n2 > n1 and n3 :
   maior = n2
if n3 > n1 and n2:
   maior = n3

if n1 < n2 and n3:
    menor = n1
if n2 < n1 and n3 :
    menor = n2
if n3 < n1 and n2:
    menor = n3

print('Maior numero : {} Menor numero : {}  '.format(maior,menor))