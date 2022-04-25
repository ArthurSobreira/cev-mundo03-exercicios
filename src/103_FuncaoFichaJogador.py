def ficha(nome, gols):
    if (nome == '') or (gols == ''):
        if nome == '':
            nome = '<desconhecido>'
        if gols == '':
            gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = input('Número do Jogador: ').title().strip()
g = input('Número de Gols: ')
if not g.isnumeric():
    g = 0
print(ficha(n, g))
