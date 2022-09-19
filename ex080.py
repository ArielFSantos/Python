lista=[]
maior = 0
menor = 9999
aux = 0
for c in range (0,5):
    aux=(int(input('Digite Valor : ')))

    if c == 0 or aux > lista[c-1]:
        lista.append(aux)
    else:
        pos = 0
        while pos < len(lista):
            if aux <= lista[pos]:
                lista.insert(pos,aux)
                break
            pos+=1






print(lista)