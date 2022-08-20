num = int(input("Digite um Numero  Decimal : "))
bin=[]
i=0
while num>1:
    i=i+1
    num=num-1

    if num % 2 == 0:
      bin[i]=0
    else:
      bin[i]=1

    for i in range(1, num):

        print(bin[i])