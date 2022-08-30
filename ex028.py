import random

sorte = random.randint(0,5)
print(sorte)

number=int(input("Digite O Numero da Sorte : "))

while number != sorte:

    number = int(input("Numero Incorreto Voce Errou.\nDigite O Numero da Sorte : "))

    if number == sorte:
        print("Parabens voce Acertou")