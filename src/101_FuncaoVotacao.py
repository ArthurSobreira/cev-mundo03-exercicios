def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
     return 'Não Vota!'
    if 18 <= idade <= 65:
     return 'Voto Obrigatório!'
    if (idade > 65) or (16 <= idade < 18):
     return 'Voto Opcional!'


ano = int(input('Em que ano você nasceu?: '))
print(voto(ano))
