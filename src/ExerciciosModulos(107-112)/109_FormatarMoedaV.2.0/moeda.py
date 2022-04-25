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
