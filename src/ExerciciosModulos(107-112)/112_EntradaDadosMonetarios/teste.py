from utilidadescev import dados, moeda

num = dados.leiaDinheiro('Digite o preço: R$')
aum = dados.leiaDinheiro('Qual a porcentagem de aumento?: ')
dim = dados.leiaDinheiro('Qual a porcentagem de redução?: ')
moeda.resumo(num, aum, dim)
