from matplotlib import pyplot as plt
from wordcloud import WordCloud
from num2words import num2words
from random import randint
from faker import Faker

nomes = []
pont = []
namePont = []
def Histograma():
    plt.hist(pont,density=True)
    plt.title('Histograma das Pontuações')
    plt.ylabel('Probabilidade')
    plt.xlabel('Pontuações')
    plt.grid("5")
    plt.show()
def wc():
    for c in pont:
        namePont.append(num2words(c, lang='pt-br').title())
    itens = " ".join(p for p in namePont)
    wordcloud = WordCloud().generate(itens)
    wordcloud.to_file("WorldCloud.jpg")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


fk = Faker()
with open("dados.txt",'w') as arquivo:
    for c in range(0, 50):
        arquivo.write(fk.name() + str(randint(1,11)) +'\n')
with open("dados.txt",'r') as arquivo:
    for v in arquivo:
        nomes.append(v[:-2])
        pont.append(int(v[-2]))

Histograma()
wc()

