import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')

aum = float(input('Qual a porcentagem de aumento?: '))
print(f'Aumentando {aum}%, temos {moeda.moeda(moeda.aumentar(num, aum))}')

dim = float(input('Qual a porcentagem de redução?: '))
print(f'Ruduzindo {dim}%, temos {moeda.moeda(moeda.diminuir(num, dim))}')
