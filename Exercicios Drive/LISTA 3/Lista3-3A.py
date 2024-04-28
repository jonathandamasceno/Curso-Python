def multnumeros(num):
    n = 0
    for n in range(0, 101):
        print(num * n)


def validador(num):
    if 1 <= num <= 100:
        return True
    

if __name__ == '__main__':
    while True:
        entrada = int(input('Digite um numero de 1 a 100: '))
        if validador(entrada):
            break
        else: 
            print('Digite um número corretamente')
    multnumeros(entrada)
            