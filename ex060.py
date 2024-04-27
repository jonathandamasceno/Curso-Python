num = int(input('DIGITE UM NUMERO: '))
c = num
fat = num
while c != 1:
    c -= 1
    fat *= c
print('O fatorial de {} é {}'.format(num, fat))
    