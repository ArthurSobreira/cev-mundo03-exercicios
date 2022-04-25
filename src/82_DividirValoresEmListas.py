list_com = []
list_par = []
list_ímpar = []
while True:
    num = int(input('Digite um valor: '))
    list_com.append(num)
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

for c in list_com:
    if c % 2 == 0:
        list_par.append(c)
    else:
        list_ímpar.append(c)
print(f'A lista completa é {list_com}.')
print(f'A lista de pares é {list_par}.')
print(f'A lista de ímpares é {list_ímpar}.')
