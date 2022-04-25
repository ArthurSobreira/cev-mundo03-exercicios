def dataExi(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError, FileExistsError):
        return False
    else:
        return True


def createArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')


def readArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o aquivo!')
    else:
        cont = 0
        for l in a:
            data = l.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:3>} anos')
            cont += 1
        if cont == 0:
            print('Ainda não temos pessoas cadastradas')
    finally:
        a.close()


def insert(aqr, n, y):
    try:
        a = open(aqr, 'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{n};{y}\n')
        except:
            print('Erro na escrita dos dados!')
        else:
            print(f'\033[97mCadastro de {n} realizado com sucesso!!\033[m')
