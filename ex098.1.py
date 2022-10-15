import time
def contagem(inicio,fim,passo):
    print('-=' * 20)
    for c in range(inicio,fim+1,passo):
        print(c, end=' ')
        time.sleep(0.5)
    print('FIM!')


print('-=' * 20)
inicio=int(input('Inicio: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))
contagem(inicio,fim,passo)
print('-=' * 20)