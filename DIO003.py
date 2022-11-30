n = int(input('Vezes: '))

while(n > 0):
    A = input('A: ')
    B = input('B: ')

    print(A[len(B):])

    if B == A[len(B):]:
        print('encaixa')
    else:
        print('nao encaixa')
    n -= 1