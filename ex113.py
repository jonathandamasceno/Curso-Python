def leiaint(n):
    while True:
            try:
                n = int(input(f'{n}'))
            except ValueError:
                print('\033[1;96mDigite um valor inteiro válido.\033[m')
            else:
                return n


def leiareal(n):
    while True:
        try:
            n = float(input(f'{n}'))
        except ValueError:
            print('\033[1;96mDigite um valor real corretamente.\033[m')
        else:
            return n

i = leiaint('Digite um Inteiro: ')
r = leiareal('Digite um Real: ')
print('-' * 40)
print(f'O número inteiro digitado foi {i} e o real foi {r}')
print('-' * 40)
