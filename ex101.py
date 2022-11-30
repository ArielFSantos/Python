def voto(age):
    idade = 2022 - age
    if idade < 16:
        print("Voce é Muito Novo Nao Precisa Votar")
    elif idade < 18 and idade > 15:
        print("Voto facultativo 1")
    elif idade > 17 and idade < 70:
        print("Voto Obrigatorio")
    else:
        print("Voto Facultativo 2")

age = int(input("Ano de Nascimento: "))
voto(age)