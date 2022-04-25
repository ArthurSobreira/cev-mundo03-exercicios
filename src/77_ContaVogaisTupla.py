tuple_words = ('APRENDER','PROGRAMAR', 'ESTUDAR', 'PRATICAR', 'CONSTRUIR', 'FUTURO', 'LINGUAGEM')
tuple_vowels = ('A', 'E', 'I', 'O', 'U')

temp = 0
for c in tuple_words:
    print(f'As vogais da palavra {c} são: ', end='')
    for i in c:
        if i in tuple_vowels:
            if temp != i:
                print(f'{i}', end =' ')
            temp = i
    print('\n')
