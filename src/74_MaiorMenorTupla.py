from random import randint

print('=' * 18)
print('Valores Sorteados:')
print('=' * 18)

num_sort = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
maior_num = 0
menor_num = 0
for c, i in enumerate(num_sort):
    print(i)
    if c == 0:
        maior_num = i
        menor_num = i
    if i > maior_num:
        maior_num = i
    if i < menor_num:
        menor_num = i

print('=' * 28)
print(f'O maior valor sorteado foi {maior_num}')
print(f'O menor valor sorteado foi {menor_num}')
print('=' * 28)

print('=' * 28)
print(f'O maior valor sorteado foi {max(num_sort)}') # Ultilizando o Método MAX.
print(f'O menor valor sorteado foi {min((num_sort))}') # Ultilizando o Método MIN.
print('=' * 28)
