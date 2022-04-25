player = dict()
partidas = list()
player['Nome'] = str(input('Nome do Jogador: ')).strip().title()
quant = int(input(f'Quantas partidas {player["Nome"]} jogou?: '))
for c in range(1, (quant + 1)):
    gols = int(input(f'Gols na {c}º Partida: '))
    partidas.append(gols)
player['Gols'] = partidas
player['Total'] = sum(partidas) #Soma dos items de partidas.
print('=' * 60)
print(player)
print('=' * 60)
for key, val in player.items():
    print(f'O campo {key} tem valor {val}.')
print('=' * 60)
print(f'O jogardor {player["Nome"]} jogou {len(player["Gols"])} partidas.')
for ind, val in enumerate(player['Gols']):
    print(f'     > Na partida {ind+1}, marcou {val} gols.')
print(f'Fez um total de {player["Total"]} gols.')
