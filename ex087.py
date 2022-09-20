matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = soma = maior = 0
for a in range (0,3):
    for b in range(0, 3):
        matriz[a][b] = int(input('Digite Numero : '))
        if a == 1 and b == 0:
            maior=matriz[a][b]
        else:
            if maior < matriz[1][b]:
                maior = matriz[1][b]

        if matriz[a][b] % 2 == 0:
            par += matriz[a][b]
        if b == 2:
            soma+=matriz[a][b]
for a in range(0,3):
    for b in range(0,3):
        print(f'{[matriz[a][b]]}',end='')
    print()
print(f'A Soma dos Valores Pares : {par}')
print(f'A Soma da Terceira Coluna : {soma}')
print(f'O Maior Valor da Segunda Linha : {maior}')