from random import choice

f1 = str(input("Digite Filme 1 : "))
f2 = str(input("Digite Filme 2 : "))
f3 = str(input("Digite Filme 3 : "))

listaFilmes=[f1,f2,f3]

sorte = choice(listaFilmes)

print(sorte)