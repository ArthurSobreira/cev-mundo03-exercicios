from random import randint
from time import sleep
list = []
print('=' * 35)
print(f'{"Sorteador Mega Sena":^35}')
print('=' * 35)
quant_sort = int(input('Quantos jogos você deseja sortear?: '))
print('=' * 35)
for c in range(0, quant_sort):
    game = []
    for i in range(0, 6):
        num = randint(1, 60)
        if num in game:
            while num in game:
                num = randint(1, 60)
            game.append(num)
        else:
            game.append(num)
        game.sort()
    list.append(game)
    print(f'Jogo {c + 1}: {game}')
    sleep(1)
print('=' * 35)
print(f'{"<<< Boa sorte no Jogo >>>":^35}')
print('=' * 35)
