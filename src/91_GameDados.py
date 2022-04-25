from random import randint
from time import sleep

games = dict()
nums = list()
for c in range(1, 5):
    games[f'Jogador_{c}'] = randint(1, 6)
print(f'{"Valores Sorteados:":^28}')
print('=' * 28)
for key, val in games.items():
    print(f'O {key} tirou {val} no dado.')
    nums.append(val)
    sleep(1)
print()
print(f'{"Ranking dos Jogadores:":^28}')
print('=' * 28)
for c in range(1, 5):
    maior_val = max(nums)
    print(f'{c}º Lugar: ', end='')
    for j in games:
        if games[j] == maior_val:
            print(f'{j} com {maior_val}.')
            nums.remove(maior_val)
            games.pop(j)
            sleep(1)
            break


# Utilizando itemgetter

from random import randint
from time import sleep
from operator import itemgetter

games = dict()
rank = list()
for c in range(1, 5):
    games[f'Jogador_{c}'] = randint(1, 6)
print(f'{"Valores Sorteados:":^28}')
print('=' * 28)
for key, val in games.items():
    print(f'O {key} tirou {val} no dado.')
    sleep(1)
print()
print(f'{"Ranking dos Jogadores:":^28}')
print('=' * 28)
rank = sorted(games.items(), key=itemgetter(1), reverse=True)
for ind, val in enumerate(rank):
    print(f'{ind+1}º Lugar: {val[0]} com {val[1]}.')
    sleep(1)
