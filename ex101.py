def voto(age):
    idade = 2022 - age
    if idade < 16:
        return "Voce é Muito Novo Nao Precisa Votar"
    elif 16 >= idade < 18 or idade > 65:
        return "Voto facultativo 1"
    else:
        return 'Voto Obrigatorio'


age = int(input("Ano de Nascimento: "))
print(voto(age))