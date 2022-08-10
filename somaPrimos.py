num = int(input('Digite um numero: '))
numero = num
soma = num

while num>1:
    num=num-1
    cont=1
    for i in range(1,num):
        if num % i == 0:
            cont=cont+1
    if (cont==2):
        soma=soma+num

print(soma)
