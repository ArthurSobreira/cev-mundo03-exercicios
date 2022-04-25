list = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        list[0].append(num)
    else:
        list[1].append(num)
list[0].sort()
list[1].sort()
print(f'Os valores pares digitados foram: {list[0]}')
print(f'Os valores ímpares digitados foram: {list[1]}')
