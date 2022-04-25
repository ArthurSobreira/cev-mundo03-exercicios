aluno = {}
aluno['Nome'] = str(input('Nome do aluno: ')).title()
aluno['Média'] = float(input(f'Média de {aluno.get("Nome")}: '))
print('=' * 30)
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for key, val in aluno.items():
    print(f'{key} é igual a {val}.')
