def subconjuntos(numeros):
    return subconjuntos1([],sorted(numeros))

def subconjuntos1(atual, conjunto):
    if conjunto:
        return subconjuntos1(atual,conjunto[1:]) + subconjuntos1(atual+[conjunto[0]],conjunto[1:])
    return [atual]

numeros = [1,2,3]
resultado = subconjuntos(numeros)
print(resultado)
