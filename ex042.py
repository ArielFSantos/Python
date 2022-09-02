n1 = int(input('Digite o Valor da Reta 1 : '))
n2 = int(input('Digite o Valor da Reta 2 : '))
n3 = int(input('Digite o Valor da Reta 3 : '))

if n1 == n2 == n3:
    print('Triangulo Equilatero')
elif n1 == n2 and n1 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n2 !=n1 :
    print('Triangulo Isosceles')
elif n1 != n2 != n3:
    print('Triangulo Escaleno')