import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, form=True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, form=True)}')

aum = int(input('Qual a porcentagem de aumento?: '))
print(f'Aumentando {aum}%, temos {moeda.aumentar(num, aum, form=True)}')

dim = int(input('Qual a porcentagem de redução?: '))
print(f'Ruduzindo {dim}%, temos {moeda.diminuir(num, dim, form=True)}')
