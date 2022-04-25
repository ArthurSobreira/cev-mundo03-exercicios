table_bra = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Fluminense', 'Corinthians', 'Internacional', 'Athletico-PR',
             'Cuiabá', 'Atlético-GO', 'São Paulo', 'Ceará', 'Santos', 'Bahia', 'Juventude', 'Grêmio', 'América-MG', 'Sport', 'Chapecoense')

print('=' * 34)
print('20 Primeiros Times do Brasileirão: ')
print('=' * 34)
for c, j in enumerate(table_bra):
    print(f'{c + 1}ª - {j}')

print('=' * 22)
print('5 Primeiros Colocados: ')
print('=' * 22)
for c, j in enumerate(table_bra):
    if 0 <= c <= 4:
        print(f'{c + 1}ª - {j}')

print('=' * 20)
print('4 Últimos Colocados:')
print('=' * 20)
for c, j in enumerate(table_bra):
    if 16 <= c <= 20:
        print(f'{c + 1}ª - {j}')

print('=' * 26)
print('Times em Ordem Alfabética:')
print('=' * 26)
for c in sorted(table_bra):
    print(c)

print('=' * 39)
position = table_bra.index('Chapecoense')
print(f'O time Chapecoense está na {position + 1}º posição.')
print('=' * 39)
