from matplotlib import pyplot as plt
from faker import Faker
from random import randint
from time import sleep
import pandas
from num2words import num2words
from wordcloud import WordCloud

# Criação de listas que serão usadas
leitura = []
nomes = []
pont = []
num = []

# Quantos nomes e números deverão ser criados aleatóriamente
n = int(input('Quantos nomes gostaria de gerar? '))
print('Gerando nomes e números aleatórios...')

# Gerar nomes e números aleatórios dentro de um arquivo txt
fake = Faker('pt_BR')
with open('dados.txt', 'w') as arquivo:
    for c in range(0, n):
        arquivo.write(f'{fake.name()},{str(randint(1, 10))},')

# Ler arquivo txt e lançar em uma lista para ser manipulado
with open('dados.txt', 'r') as arquivo:
    leitura = arquivo.read().split(',')
leitura.pop()  # Remover o último item da lista sendo um lixo gerado pela leitura

# Lançar nas listas separadas de nome e números (pontuações)
for c in range(0, (n*2), 2):
    nomes.append(leitura[c])
    pont.append(leitura[c + 1])


# Escrever o número por extenso e lançar em uma lista
for c in pont:
    num.append(num2words(c, lang='pt-br').title())

# Gerar uma string única para o wordcloud gerar a núvem
palavras = " ".join(p for p in num)
wordcloud = WordCloud(background_color="grey", width=800, height=400).generate(palavras)
wordcloud.to_file("Nuvem de palavras.jpg")

# Informar itens gerados
sleep(1)
print('Lista completa gerada:')
print(leitura)
sleep(0.5)
print('Nomes da lista gerada:')
print(nomes)
sleep(0.5)
print('Posição equivalente dos nomes gerados:')
print(pont)
sleep(0.5)
print('Número posição por extenso:')
print(num)

# Organizar a lista pont
pont.sort()
pont.sort(key=len)

# Gerar gráficos
plt.subplot(2, 1, 1)
bbin = len(pandas.unique(pont))
plt.hist(pont, bbin, density=True, facecolor='blue', label='Histograma das Pontuações')
plt.xlabel('Pontuações')
plt.ylabel('Probabilidade')
plt.grid(True)
plt.subplot(2, 1, 2)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=1)
plt.show()