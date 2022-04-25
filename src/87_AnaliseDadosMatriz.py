matriz = [[], [], []]
prin_dia = sec_dia = 1
for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite o valor para [{c}, {i}]: '))
        if c == i:
            prin_dia *= num
        if (c == 0 and i == 2) or (c == 1 and i == 1) or (c == 2 and i == 0):
            sec_dia *= num
        matriz[c].append(num)
print('=' * 23)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}] ', end='')
    print('')
print('=' * 23)
soma_par = maior_val_lin2 = soma_ter = 0
for c in matriz:
    for i in c:
        if c == matriz[1]:
            #maior_val_lin2 = max(c)
            if i == 0:
                maior_val_lin2 = i
            if i > maior_val_lin2:
                maior_val_lin2 = i
        if i % 2 == 0:
            soma_par += i
        if i == c[2]:
            soma_ter += i
print(f'A soma dos valores pares digitados é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_ter}.')
print(f'O maior valor da segunda linha é {maior_val_lin2}.')
print(f'O valor do determinante da matriz é {prin_dia - sec_dia}.')
