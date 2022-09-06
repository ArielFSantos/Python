
num = int(input("Digite um Numero  Inteiro Decimal : "))
binario = []
i = 0
while num > 0:

    if num % 2 == 0:
        binario[i] = 0
    else:
        binario[i] = 1
num = num /2
i = i +1
print(binario[i],end='')

