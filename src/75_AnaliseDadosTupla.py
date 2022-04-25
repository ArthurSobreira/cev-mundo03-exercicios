pri_num = int(input('Digite o primeiro número: '))
seg_num = int(input('Digite o segundo número: '))
ter_num = int(input('Digite o terceiro número: '))
qua_num = int(input('Digite o quarto número: '))

tuple = (pri_num, seg_num, ter_num, qua_num)

print('=' * 27)
print(f'Os valores digitados foram:')
print('=' * 27)
for c in tuple:
    print(c)

# Contar quantas vezes o 9 aparece na tupla.
cont_9 = tuple.count(9)
if cont_9 == 1:
    print(f'O valor 9 apareceu {cont_9} vez.')
if cont_9 > 1:
    print(f'O valor 9 apareceu {cont_9} vezes.')
if cont_9 == 0:
    print(f'O valor 9 não apareceu nenhuma vez.')

# Mostrar a posição do número 3 na tupla.
if 3 in tuple:
    for c, j in enumerate(tuple):
        if j == 3:
            print(f'O valor 3 apareceu na posição {c + 1}.')
else:
    print('O valor 3 não apareceu nenhuma vez.') # Caso o número 3 não esteja na tupla.

# Mostrar os números pares digitados.
cont_pares = 0
for c in tuple:
    if c % 2 == 0:
        cont_pares += 1

if cont_pares == 1: # Caso tenha apenas um número par.
    print('O valor par digitado foi ', end='')
    for c in tuple:
        if c % 2 == 0:
            print(f'{c}', end=' ')
if cont_pares > 1: # Caso tenha mais de um número par.
    print('Os valores pares digitados foram: ', end='')
    for c in tuple:
        if c % 2 == 0:
            print(f'{c}', end=' ')
if cont_pares == 0: # Caso não tenha nenhum número par.
    print('Não foram digitados número pares.')
