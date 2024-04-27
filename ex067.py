c = 0
while True:
    num = int(input('DIGITE UM NUMERO E EU FAREI A TABUADA (numero negativo para): '))
    if num < 0:
        break
    for c in range(1, 11):
        print('{} X {} = {}'.format(num, c, (num*c)))
print('Fim do programa.')