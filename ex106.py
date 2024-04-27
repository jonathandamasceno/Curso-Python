def ajuda():
    print('\033[1;44m', end='')
    print('=' * 40)
    print(" Sistema de ajuda ao usuário ")
    print('=' * 40)
    print('\033[m', end='')
    while True:
        fb = str(input('Digite a função ou biblioteca: ')).strip().lower()
        while fb in '':
            fb = str(input('Digite a função ou biblioteca: ')).strip().lower()
        if fb in 'fim':
            break

        print('\033[2;47m', end='')
        print('=' * 40)
        print(f" Acessando o manual do comando {fb}. ")
        print('=' * 40)
        print('\033[m', end='')
        print('\033[2;43m', end='')
        print(f'{help(fb)}')
        print('\033[m', end='')


ajuda()
