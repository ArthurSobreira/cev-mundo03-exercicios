grupo = list()
idade = list()
cad_fem = list()
c = 1
while True:
    print('=' * 25)
    print(f'   Cadastro {c}º Pessoa:')
    print('=' * 25)
    cad = dict()
    cad['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            cad['Sexo'] = sexo
            if cad['Sexo'] == 'F':
                cad_fem.append(cad['Nome'])
            break
        print('Dado inválido, digite apenas M ou F.')
    cad['Idade'] = int(input('Idade: '))
    idade.append(cad['Idade'])
    grupo.append(cad)
    while True:
        stop = str(input('Deseja Continuar?[S/N]: ')).strip().upper()[0]
        if stop in 'SN':
            break
        print('Dado inválido, digite apenas S ou N.')
    if stop == 'S':
        c += 1
    if stop == 'N':
        break
print('=' * 50)

# Quantidade de pessoas no grupo...
print(f' > O grupo tem {len(grupo)} pessoas cadastradas.')

# Média das idades...
méd = (sum(idade)) / (len(idade))
print(f' > A média de idade é de {méd:.2f} anos.')

#Nome das mulheres cadastradas...
if len(cad_fem) > 1:
    print(' > As mulheres cadastradas foram: ', end='')
    for name in cad_fem:
        print(f'{name}...', end='')
    print()
if len(cad_fem) == 1:
    print(f' > A mulher cadastrada foi {cad_fem[0]}.')
if len(cad_fem) == 0:
    print(' > Não foi cadastrada nenhuma mulher.')

#Pessoas acima da média de idade...
print(' > Lista das pessoas acima da média de idade: ')
for dic in grupo:
    for val in dic:
        if val == 'Idade':
            if dic['Idade'] > méd:
                print('     ', end='')
                for key, val in dic.items():
                    print(f'{key}: {val}', end='; ')
                print()
