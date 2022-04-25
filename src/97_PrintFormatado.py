def escreva(msg):
    size = len(msg) + 4
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


while True:
    mens = str(input('Digite algo (Zero para sair): ')).title()
    if mens == 'Zero':
        break
    escreva(mens)
escreva('Obrigado, volte sempre!!')
