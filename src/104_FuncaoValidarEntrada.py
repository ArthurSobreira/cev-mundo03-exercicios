def leiaInt():
    while True:
        num = input('Digite um Número: ')
        if num.isnumeric():
            break
        print('\033[31mErro, digite um número inteiro válido!\033[m')
    return f'Você acabou de digitar o número {num}.'

print(leiaInt())



def leiaInt2(msg):
    ok = False
    val = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            val = int(n)
            ok = True
        else:
            print('\033[31mErro, digite um número inteiro válido!\033[m')
        if ok:
            break
    return val


nu = leiaInt2('Digite um número: ')
print(f'Você acabou de digitar o número {nu}')
