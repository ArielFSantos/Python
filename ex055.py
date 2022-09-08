max = 0
min = 0
for c in range (0,5):
    peso = float(input("Digite Seu Peso : "))

    if peso > max:
        max = peso
    if peso < min:
        min = peso

print('Peso Maximo : {} KGs \nPeso Minimo : {} KGs'.format(max,min))