my_list = []
for c in range(0, 5):
    num = int(input(f'Digite um valor para a posição {c}: '))
    my_list.append(num)

print('=' * 33)
print(f'O valores digitados foram: {my_list}')

if my_list.count(max(my_list)) == 1: # Caso tenha apenas um número maior
    print(f'O maior valor digitado foi {max(my_list)}, na posição {my_list.index(max(my_list))}...')

else: # Caso o maior número apareça mais de uma vez
    print(f'O maior valor digitado foi {max(my_list)}, nas posições ', end='')
    for i, c in enumerate(my_list):
        if c == max(my_list):
            print(f'{i}', end='...')

if my_list.count(min(my_list)) == 1: # Caso tenha apenas um número menor
    print(f'\nO menor valor digitado foi {min(my_list)}, na posição {my_list.index(min(my_list))}...')

else: # Caso o menor número apareça mais de uma vez
    print(f'\nO menor valor digitado foi {min(my_list)}, nas posições ', end='')
    for i, c in enumerate(my_list):
        if c == min(my_list):
            print(f'{i}', end='...')
