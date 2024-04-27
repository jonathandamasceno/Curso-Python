def leiaint(frase):
    frase = str(input('Digite um Número: '))
    if frase.isnumeric():
        return frase
    else:
        while True:
            print('\033[031mERRO!! DIGITE UM NÚMERO VÁLIDO.\033[m')
            frase = str(input('Digite um Número: '))
            if frase.isnumeric():
                return frase


n = leiaint('Digite um Número: ')
print(f'O número digitado foi {n}')
