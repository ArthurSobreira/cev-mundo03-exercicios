from random import randint


def sort(list):
    for c in range(5):
        list.append(randint(1, 10))
    print('Sorteando 5 Valores da lista: ', end='')
    for i in list:
        print(f'{i}', end='...')
    print('Pronto!')


def somaPar(list):
    print(f'Somando os valores pares de {list}, temos ',end='')
    soma = 0
    for c in list:
        if c % 2 == 0:
            soma += c
    print(f'{soma}.')

números = list()
sort(números)
somaPar(números)
