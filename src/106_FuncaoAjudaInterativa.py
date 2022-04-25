from time import sleep


def separador(mensagem, cor):
    size = len(mensagem) + 20
    print(f'\033[{cor};1m=\033[m' * size)
    print(f'\033[{cor};1m{mensagem:^{size}}\033[m')
    print(f'\033[{cor};1m=\033[m' * size)


def ajuda(comand):
    print('\033[107;30m')
    help(comand)
    print('\033[m')


while True:
    separador('SISTEMA DE AJUDA PyHELP', 42)
    sleep(1)
    print()
    com = str(input('Fução ou bibioteca (Digite "fim" para sair): ')).lower()
    print()
    if com == 'fim':
        break
    separador(f'Acessando o manual do comando "{com}"', 44)
    sleep(1)
    print()
    ajuda(com)

separador('Até Logo!!', 41)
