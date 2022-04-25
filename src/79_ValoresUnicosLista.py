list = []
while True:
    num = int(input('Digite um valor: '))
    if not num in list:
        list.append(num)
        resp = str(input('Valor Adicionado, deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        resp = str(input('Valor Repetido (Não adicionado), deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            break
list.sort()
print('Os valores digitados foram: ', end='')
for c in list:
    print(f'{c}', end='...')
