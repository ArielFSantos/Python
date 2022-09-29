import random
from operator import itemgetter
ranking = {}
resultados = {'player1': random.randint(1,6),
              'player2': random.randint(1,6),
              'player3': random.randint(1,6),
              'player4': random.randint(1,6)}
ranking = sorted(resultados.items(), key=itemgetter(1))



print(ranking)
print('Vencedor : {}'.format(ranking[3]))