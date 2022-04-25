from time import sleep
list = []
c = 0
while True:
    print(f'===== Cadastro Aluno {c + 1} =====')
    nome = str(input('Digite o Nome: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª Nota: '))
    list.insert(c, [nome, [nota1, nota2]])
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'S':
        c += 1
    if cont == 'N':
        break
print('=' * 41)
print(f'{"Boletim da Turma":^41}')
print('=' * 41)
print(f'{"No.":<}', f'{"Nome":^29}', f'{"Média":>7}')
print('=' * 41)
for aluno in list:
    med = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{(list.index(aluno) + 1):<}', f'{aluno[0].title():^35}', f'{med:>.1f}')
print('=' * 41)
while True:
    nota = int(input('Mostrar as notas de qual aluno?(sair = 0): '))
    if nota == 0:
        break
    if (nota > (len(list))) or (nota < 0):
        print('Aluno não encontrado, tente novamente...')
        print('.' * 41)
        sleep(2)
    else:
        print(f'As notas de {list[(nota - 1)][0]} são {list[(nota - 1)][1]}.')
        print('.' * 41)
print('\033[32mFinalizando', end='')
for p in range(3):
    print('.',end='')
    sleep(1)
print('Volte Sempre!!\033[m')
