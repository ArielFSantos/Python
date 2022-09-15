num = int(input("Digite um Numero  Inteiro Decimal : "))
binario = []

while num > 0:

        if num % 2 == 0:
            binario.append(0)
        else:
            binario.append(1)
        num = num // 2

for c in range (len(binario),0,-1):

    print(binario[c-1],end='')

