def area(larg, comp):
    área = larg * comp
    print(f'A área do terreno é {larg}x{comp} é de {área}m².')


print('Controle de Terrenos')
print('=' * 20)
la = float(input('Largura(m): '))
co = float(input('Comprimento(m): '))
area(la, co)
