def separador(msg):
    size = len(msg) + 4
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def fatorial(num, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param num: Número do qual será calculado a fatorial.
    :param show:
    Para (show) == True: Mostra o cálculo de forma detalhada, com todos os números presentees na fatorial.
    Para (show) == False: Mostra apenas o resultado da fatorial (parâmetro padrão da def).
    :return: Resultado da fatorial de (num), e, dependendo do valor lógico de (show), mostra também os cálculo completo.
    '''
    c = num
    fact = 1
    cont = 0
    for c in range(c, 0, -1):
        fact *= c
        if show == True:
            print(f'{c}', end='')
            cont += 1
            if cont < num:
                print(f' * ', end='')
    return f' = {fact}'


separador('Cáculo de uma Fatorial')
num = int(input('Digite um número: '))
print(f'A fatorial de {num}{fatorial(num)}.')
while True:
    show = str(input('Deseja mostrar os passos da fatorial? [S/N]: ')).strip().upper()[0]
    if show in 'SN':
        break
    print('Dado inválido, digite apenas "S" ou "N".')
if show == 'S':
    print(fatorial(num, True))
separador('Programa Encerrado, Volte Sempre!!')
