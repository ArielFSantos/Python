cadastroF = []
cadastrogeralF = []
temp=[]
cadastroT = {}
id = 0
def cadastroFerramentas(choice):

    temp.append(id)
    cadastrogeralF.append(temp[:])
    temp.clear()
    print(cadastrogeralF)

choice = int(input('Opções \n1 Cadastro de Ferramentas \n2 Cadastro de Técnicos\n'))
while True:
    if choice == 1:
        id += 1
        cadastroFerramentas(choice)
    choice = int(input('Opções \n1 Cadastro de Ferramentas \n2 Cadastro de Técnicos\n'))
