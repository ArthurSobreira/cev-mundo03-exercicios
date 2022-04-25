list = []
c = 1
while True:
    person = []
    print('=' * 29)
    print(f'      Cadastro pessoa {c}')
    print('=' * 29)
    person.append(str(input('Nome: ')).title())
    person.append(float(input('Peso: ')))
    list.append(person)
    cont = str(input(('Deseja continuar? [S/N]: '))).strip().upper()[0]
    if cont == 'N':
        break
    if cont == 'S':
        c += 1
print('')
print(f'Ao todo, foram cadastradas {len(list)} pessoas.')
maior_peso = list[0][1]
menor_peso = list[0][1]
for i in list:
    if i[1] >= maior_peso:
        maior_peso = i[1]
    if i[1] <= menor_peso:
        menor_peso = i[1]
print(f'O maior peso foi de {maior_peso}Kg, peso de ', end='')
for i in list:
    for j in i:
        if j == maior_peso:
            print(f'{i[0]}', end='...')

print(f'\nO menor peso foi de {menor_peso}Kg, peso de ', end='')
for i in list:
    for j in i:
        if j == menor_peso:
            print(f'{i[0]}', end='...')
