num = []
def maior(numeros):
    maiorNum = num[0]
    for c in range (0,len(num)):
        if num[c] > maiorNum:
            maiorNum = num[c]
    print(f'O Maior Numero é: {maiorNum}')


while True:
    aux = int(input('Numero: '))
    if aux == 0:
        break
    num.append(aux)
maior(num)