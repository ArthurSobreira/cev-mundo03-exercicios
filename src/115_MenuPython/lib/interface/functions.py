from time import sleep
from lib.file.data import *

def colour(msg, cor):
    '''
    -> Função para colorir um texto.
    :param msg: Texto a ser colorida.
    :param cor: Cor do texto.
    :return: Texto colorido com a cor escolhida.
    '''
    return f'\033[{cor}m{msg}\033[m'


def apart(msg, apa, cor=32):
    '''
    -> Função para separar um texto com o caractere desejado.
    :param msg: Texto a ser separado.
    :param apa: Caráctere separador.
    '''
    size = 42
    print(colour(apa * size, 97))
    print(colour(f'{msg.upper():^{size}}', cor))
    print(colour(apa * size, 97))


def select(msg):
    '''
    -> Função para validar o input de um valor, a função irá aceitar apenas os números 1, 2 ou 3.
    :param msg: Mensagem que irá receber o input.
    '''
    while True:
        try:
            choice = int(input(msg))
        except (ValueError, TypeError):
            print(colour('Erro, dado inválido, Tente Novamente!', 31))
            continue
        else:
            if choice in range(1, 4):
                if choice == 1:
                    choice1()
                    break
                if choice == 2:
                    choice2()
                    break
                if choice == 3:
                    choice3()
                    break
            else:
                print(colour('Erro, dado inválido, Tente Novamente!', 31))
                continue


def cad():
    '''
    -> Função para exibir o Menu Principal.
    '''
    apart('menu principal', '=')
    print(colour('1 - ', 33), end=''), print(colour('Ver pessoas cadastradas', 34))
    print(colour('2 - ', 33), end=''), print(colour('Cadastrar nova Pessoa', 34))
    print(colour('3 - ', 33), end=''), print(colour('Sair do Sistema', 34))
    print(colour('=' * 42, 97))
    select(colour('SUA ESCOLHA: ', 97))


arq = 'data.txt'
def choice1():
    '''
    -> Para caso a escolha do usário seja '1', mostra na tela as pessoas cadastradas.
    :return: Retorna o Menu de Cadastro novamente.
    '''
    apart('Pessoas Cadastradas', '=', 36)
    if not dataExi(arq):
        createArq(arq) # Caso o arq.txt não exista, o função ira cria-lo.
    readArq(arq)
    sleep(1)
    return cad()


def choice2():
    '''
    -> Para caso a escolha do usuário seja '2', cadastra uma nova pessoa.
    :return: Retorna o Menu de Cadastro novamente.
    '''
    apart('Novo Cadastro', '=', 35)
    while True:
        try:
            name = str(input(colour('NOME: ', 97))).title().strip()
        except TypeError:
            print(colour('Nome Inválido, Tente Novamente.', 31))
        else:
            if (name.isalpha()) or (' ' in name):
                break
            else:
                print(colour('Nome Inválido, Tente Novamente.', 31))
                continue
    while True:
        try:
            age = int(input(colour('IDADE: ', 97)))
        except (ValueError, TypeError):
            print(colour('Idade Inválida, Tente Novamente.', 31))
            continue
        else:
            break
    insert(arq, name, age)
    sleep(1)
    return cad()


def choice3():
    '''
    -> Encerra o programa com uma mensagem de despedida.
    '''
    apart('Fim do Programa, Volte Sempre!!!', '=', 31)
