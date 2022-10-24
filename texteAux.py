import matplotlib.pyplot as plt

dias = []
aliment = []
vest = []
transp = []


quantdias = int(input('Quantos dias: '))

for c in range(c,quantdias):

    dias.append(c)
    aux = int(input(f'Gasto dia {c} Com Alimentação: '))
    aliment.append(aux)
    aux = int(input(f'Gasto dia {c} Com Vestuario: '))
    vest.append(aux)
    aux = int(input(f'Gasto dia {c} Com Transporte: '))
    transp.append(aux)

