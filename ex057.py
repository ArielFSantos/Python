sx = input('Digite [M ou F] : ').upper()

while sx not in 'MmFf':
    sx = input('Digite [M ou F] : ').upper()
print('Sexo {} Registrado'.format(sx))