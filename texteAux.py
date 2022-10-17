cadastroF = []
cadastrogeralF = []
temp =[]
cadastroT = {}
id = 0
def cadastroFerramentas(choice):
    temp.append(id)
    temp.append(input('Descrição da Ferramenta: '))
    temp.append(input('Fabricante: '))
    temp.append(input('Voltagem de Uso: '))
    temp.append(input('Part Number: '))
    temp.append(input('Tamanho: '))
    temp.append(input('Unidade de Medida: '))
    temp.append(input('Tipo de Ferramenta: '))
    temp.append(input('Material da Ferramenta: '))
    temp.append(input('Tempo Maximo de Reserva: '))
    cadastrogeralF.append(temp[:])
    temp.clear()
    print(cadastrogeralF)



def cadastroTecnicos(choice):
    cadastroT.append(input('Digite Seu Nome: '))
    cadastroT.append(input('Digite Seu CPF: '))
    cadastroT.append(input('Digite Seu Telefone Celular ou Rádio: '))
    cadastroT.append(input('Digite Seu Turno: '))
    cadastroT.append(input('Digite O Nome da Equipe: '))
    print(cadastroT)
while True:
    print('-=*' * 15)
    choice = int(input('Opções \n1 Cadastro de Ferramentas \n2 Cadastro de Técnicos\n'))
    while choice < 1 or choice > 5:
        print('-=*' * 15)
        print('Valor Incorreto, Digite Novamente.')
        choice = int(input('Opções \n1 Cadastro de Ferramentas \n2 Cadastro de Técnicos\n'))
    if choice == 1:
        id+=1
        cadastroFerramentas(choice)
    if choice == 2:
        cadastroTecnicos(choice)
