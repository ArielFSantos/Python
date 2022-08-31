sal = float(input('Digite seu salario : '))
if sal > 1250:
    aumento = sal * 0.10
else:
    aumento =  sal *0.15

print('Salario Anterior R${:.2f} Salario Atual R${:.2f} Aumento R${:.2f}'.format(sal,(sal+aumento),aumento))