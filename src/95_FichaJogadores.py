from time import sleep

time = []
while True:
    print('=' * 30)
    player = dict()
    partidas = list()
    player['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    quant = int(input(f'Quantas partidas {player["Nome"]} jogou?: '))
    for c in range(1, (quant + 1)):
        gols = int(input(f'Gols na {c}º Partida: '))
        partidas.append(gols)
    player['Gols'] = partidas
    player['Total'] = sum(partidas)  # Soma dos items de partidas.
    time.append(player)
    while True:
        stop = str(input('Deseja Continuar?[S/N]: ')).strip().upper()[0]
        if stop in 'SN':
            break
        print('Dado inválido, digite apenas S ou N.')
    if stop == 'N':
        break
print('')
print('=' * 46)
print(f'{"Cód":<}', f'{"Nome":^20}', f'{"Gols":>4}', f'{"Total":>16}')
print('=' * 46)
for ind, dict in enumerate(time):
    print(f'{(ind + 1):<}', f'{dict["Nome"]:>14}         ', end='')
    esp = 0
    for val in dict:
        if val == 'Gols':
            for gols in dict['Gols']:
                print(f'{gols}', end='.')
                esp += 2
    print(' ' * (19 - esp), f'{dict["Total"]}')
print('=' * 46)
while True:
    dados = int(input('Mostrar dados de qual jogador(0 para encerrar): '))
    if dados == 0:
        print('=' * 46)
        break
    if (dados > len(time)) or (dados < 0):
        print(f'Jogador {dados} não encontrado, tente novamente.')
        print('=' * 46)
        sleep(2)
    else:
        print(f'Levantamento do jogador \033[31m{time[dados - 1]["Nome"]}\033[m:')
        for ind, val in enumerate(time[dados - 1]['Gols']):
            print(f'   Na partida {ind + 1}, marcou {val} gols.')
        print('=' * 46)
print('\033[32mEncerrando', end='')
for c in range(3):
    print('.', end='')
    sleep(1)
print('VOLTE SEMPRE!!')
