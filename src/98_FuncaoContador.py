from time import sleep


def separador(msg):
    size = len(msg) + 6
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def contador(ini, fim, pas):
    if (ini < fim) and (pas >= 0):
        if pas == 0:
            pas = 1
        for c in range(ini, (fim + pas), pas):
            if c <= fim:
                print(f'{c}', end='...')
                sleep(0.4)
    if (ini < fim) and (pas < 0):
        pas *= -1
        for c in range(ini, (fim + pas), pas):
            if c <= fim:
                print(f'{c}', end='...')
                sleep(0.4)
    if (ini > fim) and (pas <= 0):
        if pas == 0:
            pas = -1
        for c in range(ini, (fim + pas), pas):
            if c >= fim:
                print(f'{c}', end='...')
                sleep(0.4)
    if (ini > fim) and (pas > 0):
        pas *= (-1)
        for c in range(ini, (fim + pas), pas):
            if c >= fim:
                print(f'{c}', end='...')
                sleep(0.4)
    print('Fim!!')


separador('Contagem de 1 até 10, pulando de 1 em 1:')
contador(1, 10, 1)
print()

separador('Contagem de 10 até 0, voltando de 2 em 2:')
contador(10, 0, -2)
print()

separador('Agora é sua vez de personalizar a contagem!!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio < fim:
    if passo < 0:
        passop = passo * (-1)
        separador(f'Contagem de {inicio} até {fim}, pulando de {passop} em {passop}:')
    if passo > 0:
        separador(f'Contagem de {inicio} até {fim}, pulando de {passo} em {passo}:')
    if passo == 0:
        separador(f'Contagem de {inicio} até {fim}, pulando de 1 em 1:')
else:
    if passo < 0:
        passop = passo * (-1)
        separador(f'Contagem de {inicio} até {fim}, voltando de {passop} em {passop}:')
    if passo > 0:
        separador(f'Contagem de {inicio} até {fim}, voltando de {passo} em {passo}:')
    if passo == 0:
        separador(f'Contagem de {inicio} até {fim}, voltando de 1 em 1:')
contador(inicio, fim, passo)
