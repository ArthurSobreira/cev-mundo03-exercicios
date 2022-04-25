list = []

for c in range(1, 6):
    num = int(input('Digite um valor: '))
    if c == 1 or num > list[-1]:
        list.append(num)
        print(f'Valor adicionado ao final da lista...')
    else:
        c = 0
        while c < len(list):
            if num <= list[c]:
                list.insert(c, num)
                print(f'Valor adicionado na posição {c} da lista...')
                break
            c += 1
print(f'Os valores digitados, em ordem, foram: {list}')
