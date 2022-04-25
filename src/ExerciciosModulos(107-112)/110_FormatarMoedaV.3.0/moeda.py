def moeda(val):
    return f'R${val:.2f}'.replace('.', ',')


def metade(val, form=True):
    resul = val / 2
    if form:
        return moeda(resul)
    else:
        return resul


def dobro(val, form=True):
    resul = val * 2
    if form:
        return moeda(resul)
    else:
        return resul


def aumentar(val, porc, form=True):
    p = val * (porc/100)
    resul = val + p
    if form:
        return moeda(resul)
    else:
        return resul


def diminuir(val, porc, form=True):
    p = val * (porc/100)
    resul = val - p
    if form:
        return moeda(resul)
    else:
        return resul


def resumo(val, porcA, porcD):
    print('=' * 40)
    print(f'{"Resumo do Valor":^40}')
    print('=' * 40)
    print('Preço analizado:', f'{moeda(val).center(33)}')
    print('Dobro do Preço: ', f'{dobro(val):^33}')
    print('Metade do Preço: ', f'{metade(val):^33}')
    print(f'{porcA}% de aumento: ', f'{aumentar(val, porcA):^33}')
    print(f'{porcD}% de redução: ', f'{diminuir(val, porcD):^33}')
    print('=' * 40)
