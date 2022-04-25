# UTILIZANDO UMA TUPLA
pre_list = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

print('=' * 50)
print(f'{"Listagem de Preços":^50}')
print('=' * 50)

for c in range(0, len(pre_list)):
    if c % 2 == 0:
        print(f'{pre_list[c]:.<40}', end=' ')
    else:
        print(f'R${pre_list[c]:>7.2f}')
print('=' * 50)


# UTILIZANDO DUAS TUPLAS
nom_list = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livros')
pre_list = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)

print('=' * 50)
print(f'{"Listagem de Preços":^50}')
print('=' * 50)

for c in range(0, 9):
    print(f'{nom_list[c]:.<40} R${pre_list[c]:>7.2f}')
