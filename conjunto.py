lista = []
listaAux = []
aux = 0
while True:
    aux = int(input('Digite Conjunto: '))
    if aux == 0:
        break

    lista.append(aux)


listaAux = lista
cont = len(lista) - 1


for c in range(0,len(lista)):
    print(listaAux)
    for b in range(0,len(listaAux)):
        print(listaAux[b], end='')

    listaAux.pop()

