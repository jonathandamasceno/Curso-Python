soma = 0
for c in range(0, 6):
    num = int(input('DIGITE UM NUMERO: '))
    if num % 2 == 0:
        soma += num
print(soma)