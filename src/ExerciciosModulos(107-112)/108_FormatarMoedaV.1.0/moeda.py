def metade(val):
    return val / 2


def dobro(val):
    return val * 2


def aumentar(val, porc):
    p = val * (porc/100)
    return val + p


def diminuir(val, porc):
    p = val * (porc/100)
    return val - p


def moeda(val):
    return f'R${val:.2f}'.replace('.', ',')
