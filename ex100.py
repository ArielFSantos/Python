import random
pares=0
numeros=[]
def sorteia(numeros):
    for c in range (0,5):
        numeros.append(random.randint(0,100))
    print('Numeros Sorteados: ',numeros)
    somarPar(pares)
def somarPar(pares):
    for c in range (0,5):
        if numeros[c] % 2 == 0:
            pares = pares + numeros[c]
    print("Soma de Numeros Pares: ",pares)


sorteia(numeros)
