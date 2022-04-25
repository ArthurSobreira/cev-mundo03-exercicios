def leiaDinheiro(msg):
    va = False
    while not va:
        inp = str(input(msg)).replace(',', '.').strip()
        if inp.isalpha() or inp == '':
            print(f'\033[31mErro, "{inp}" é um valor inválido!\033[m')
        else:
            va = True
            return (float(inp))
