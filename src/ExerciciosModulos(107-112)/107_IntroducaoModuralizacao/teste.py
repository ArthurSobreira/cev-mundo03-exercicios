import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de {num} é {moeda.metade(num)}.')
print(f'O dobro de {num} é {moeda.dobro(num)}.')

aum = float(input('Qual a porcentagem de aumento?: '))
print(f'Aumentando {aum}%, temos {moeda.aumentar(num, aum)}.')

dim = float(input('Qual a porcentagem de redução?: '))
print(f'Ruduzindo {dim}%, temos {moeda.diminuir(num, dim)}.')
