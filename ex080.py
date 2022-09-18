lista=[]
maior = menor = lista
for c in range (0,5):
    lista.append(int(input('Digite Valor : ')))

    if lista[c] > maior:
        maior = lista[c]
    if lista[c]< menor:
        menor = lista[c]


print(lista)