def separador(mensagem):
    size = len(mensagem) + 19
    print('=' * size)
    print(f'{mensagem:^{size}}')
    print('=' * size)


def notas(*val, sit=False):
    '''
    -> Função para analisar as notas e situações de vários alunos
    :param val: Uma ou mais notas e situações de vários alunos.
    :param sit: Parâmetro opcional, indica se deve-se mostrar a situação.
    :return: Dicionário com as irformações sobre a turma.
    '''
    my_dict = {}
    my_dict['Total'] = len(val)
    my_dict['Maior'] = max(val)
    my_dict['Menor'] = min(val)
    my_dict['Média'] = sum(val)/len(val)
    if sit == True:
        if my_dict['Média'] >= 7:
            my_dict['Situação'] = 'Boa'
        if 6 <= my_dict['Média'] < 7:
            my_dict['Situação'] = 'Razoável'
        if my_dict['Média'] < 6:
            my_dict['Situação'] = 'Ruim'
    return my_dict


resp = notas(9, 10, 5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)