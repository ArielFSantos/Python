T = int(input())
contador = 0
for i in range(T):
    N = int(input())
    K = int(input())
    aux = N / K
    contador += int(aux)*4
    print(contador)

