matriz = [[0,0,0],[0,0,0],[0,0,0]]
a=b=c=0
for a in range(0,3):
    for b in range(0,3):

            matriz[a][b]=(int(input('Digit um Numero : ')))

for a in range(0,3):
    for b in range(0,3):
        print(f'{[matriz[a][b]]}' ,end='')
    print()