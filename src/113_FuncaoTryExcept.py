def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor Inteiro digitado foi {i} e o Real foi {f}')
