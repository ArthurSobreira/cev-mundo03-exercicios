list = []
while True:
    val = int(input('Digite um valor: '))
    list.append(val)
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Você digitou {len(list)} elementos.')
list.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {list}')
if 5 in list:
    print('O valor 5 faz parte da lista.')
if 5 not in list:
    print('O valor 5 não faz parte da lista.')
