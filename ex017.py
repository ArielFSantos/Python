from math import sqrt

oposto = float(input('Digite o Comprimento do Cateto Oposto : '))
adjacente = float(input('Digite o Comprimento do Cateto Adjacente : '))

oposto = oposto*oposto
adjacente = adjacente*adjacente
hipotenusa = oposto+adjacente

hipotenusa = sqrt(hipotenusa)

print("{:.2f}".format(hipotenusa))
