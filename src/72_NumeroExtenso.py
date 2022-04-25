num_extensive = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
                 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('O número digitado não se encontra no intervalo dado, digite novamente.')
    print(f'O número digitado foi {num_extensive[num]}')
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
