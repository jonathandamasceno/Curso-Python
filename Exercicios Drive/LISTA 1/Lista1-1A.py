def vel(e, t):
    velocidade = e / t
    return int(velocidade)
c = 0
while True:
    num1 = int(input('Digite Um Número de 1 a 500: '))
    num2 = int(input('Digite Um Número de 1 a 100: '))
    if 1 <= num1 <= 500 and 1 <= num2 <= 100: 
        break
    else:
        print('Digie os valores corretamente')
resp = vel(num1, num2)
print(resp)