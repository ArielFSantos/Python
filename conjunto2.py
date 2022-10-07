listaConjuntos = []


while True:
    num = int(input('Digite: '))

    listaConjuntos.append(num)
    aux = listaConjuntos[:]
    listaConjuntos.append(aux)

    print(listaConjuntos)