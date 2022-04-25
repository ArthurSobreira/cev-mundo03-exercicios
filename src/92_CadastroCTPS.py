from datetime import date

cad = {}
cad['Nome'] = str(input('Digite seu Nome: ')).strip().title()
nasc = int(input('Digite seu Ano de Nascimento: '))
cad['Idade'] = date.today().year - nasc
cad['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cad['CTPS'] == 0:
    print('=' * 33)
    for key, val in cad.items():
        print(f'> {key}: {val}')
else:
    cad['Contratação'] = int(input('Ano de Contratação: '))
    cad['Salário'] = float(input('Salário: R$ '))
    cad['Aposentadoria'] = (cad['Contratação'] + 35) - nasc
    print('=' * 33)
    for key, val in cad.items():
        print(f'> {key}: {val}')

