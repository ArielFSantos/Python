import random

maior = 0
menor = 11
tupla = random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)

for c in range (0,5):
         if tupla[c] < menor :
            menor = tupla[c]
         if tupla[c] > maior:
            maior = tupla[c]

print(tupla)
print(sorted(tupla))
print(menor)
print(maior)
