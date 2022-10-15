import time
print('-='*20)
for c in range (1,11):
    print(c,end=' ')
    time.sleep(0.5)
print('FIM!')
print('-='*20)
for c in range(10,-1,-2):
    print(c,end=' ')
    time.sleep(0.5)
print('FIM!')
print('-=' * 20)
print('Agora é Sua Vez!')
inicio=int(input('Inicio: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))

for c in range (inicio,fim,passo):
    print(c,end=' ')
    time.sleep(0.5)