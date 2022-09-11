num=0
while True:
    num = int(input('Digite um Numero : '))
    if num < 0:
        break
    print('_' * 15)
    for c in range (1,11):

        print('{} x {} = {} '.format(num,c,(num*c)))
    print('_' * 15)