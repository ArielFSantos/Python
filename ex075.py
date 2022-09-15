tupla = (int(input('Digite um Valor : ')),int(input('Digite outro Valor : ')),int(input('Digite outro Valor : ')),int(input('Digite outro Valor : ')))
contNove = 0
for c in range (0,4):
     if tupla[c] == 9:
          contNove += 1
     if tupla[c] % 2 == 0:
          print('Par',tupla[c])
print('posição: ',tupla.index(3))
print('Quantidade de numeros 9 : ',contNove)

