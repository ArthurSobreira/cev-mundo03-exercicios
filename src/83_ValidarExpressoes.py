list_exp = []
exp = str(input('Digite uma expressão: '))

for c in exp:
    if c == '(':
        list_exp.append(c)
    if c == ')':
        if len(list_exp) > 0:
            list_exp.pop()
        else:
            list_exp.append(')')
            break
if len(list_exp) == 0:
    print('Correta!')
else:
    print('Errada!')