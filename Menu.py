cadastroF = []
cadastroT = []
temp=[]
idF = idT = 0
def cadastroFerramentas(choice):
    temp.append(idF)
    temp.append(input('Descrição da Ferramenta: '))
    temp.append(input('Fabricante: '))
    temp.append(input('Voltagem de Uso: '))
    temp.append(input('Part Number: '))
    temp.append(input('Tamanho: '))
    temp.append(input('Unidade de Medida: '))
    temp.append(input('Tipo de Ferramenta: '))
    temp.append(input('Material da Ferramenta: '))
    temp.append(input('Tempo Maximo de Reserva: '))
    cadastroF.append(temp[:])
    temp.clear()
    print(cadastroF)
def cadastroTecnicos(choice):
    temp.append(idT)
    temp.append(input('Digite Seu Nome: '))
    temp.append(input('Digite Seu CPF: '))
    temp.append(input('Digite Seu Telefone Celular ou Rádio: '))
    temp.append(input('Digite Seu Turno: '))
    temp.append(input('Digite O Nome da Equipe: '))
    cadastroT.append(temp[:])
    temp.clear()
    print(cadastroT)
while True:
    print('-=*' * 15)
    choice = int(input('Opções \n1 Cadastro de Ferramentas \n2 Cadastro de Técnicos\n'))
    while choice < 1 or choice > 5:
        print('-=*' * 15)
        print('Valor Incorreto, Digite Novamente.')
        choice = int(input('Opções \n1 Cadastro de Ferramentas \n2 Cadastro de Técnicos\n'))
    if choice == 1:
        idF+=1
        cadastroFerramentas(choice)
    if choice == 2:
        idT+=1
        cadastroTecnicos(choice)
