from time import sleep

def maior(* val):
    print('-=' * 30)
    print('Analizando os valores passados...')
    maior_val = 0
    c = 0
    for num in val:
        print(f'{num}', end='...')
        sleep(0.5)
        if c == 0:
            maior_val = num
        else:
            if num > maior_val:
                maior_val = num
        c += 1
    print(f'\nForam informados {c} valores ao todo.')
    print(f'O maior valor informado foi {maior_val}.')
    print('-=' * 30)
    print()


maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()
