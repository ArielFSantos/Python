frase = str(input('Digite um Texto : ')).lower()
frase = frase.replace(" ","")
reversed_frase ='' .join(reversed(frase))

if frase == reversed_frase:

    print('true')
else:
    print('false')
