def validador(n):
    certo = False
    while not certo:
        num = str(input(n)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[31mErro! "{num}" não é um numero.\033[m')
        else:
            certo = True
            return float(num)
