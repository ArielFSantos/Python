lista=[]

for c in range (0,5):
    lista.append (input('Numero Inteiro : '))
print('Voce Digitou os Valores :{}'.format(lista))

listaOrd = sorted(lista)

print('Menor Numero : {} Na Posição : {}'.format(listaOrd[0],lista.index(listaOrd[0])))
print('Maior Numero : {} Na Posição : {}'.format(listaOrd[4],lista.index(listaOrd[4])))

