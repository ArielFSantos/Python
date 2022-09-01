valorCasa = int(input('Digite o Valor do Imovel : '))
salario = int(input('Digite o Salario : '))
prazo = int(input('Digite o Prazo em Meses : '))

if (valorCasa / prazo) > (salario * 0.3):
    print("Valor Excede o Maximo.\nEmprestimo Negado!")
else:
    print("Emprestimo Aprovado")