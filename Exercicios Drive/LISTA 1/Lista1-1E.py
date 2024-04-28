# q bglh dificil de entender
def converte(h, m, s):
    h = int(h)
    m = int(m)
    s = int(s)
while True:
    num = int(input('Digite os segundos: '))
    if 1 <= num <= 100000000:
        hora = num // 3600
        minuto = (num % 3600) // 60
        segundo = (num % 3600) % 60
        converte(hora, minuto, segundo)
        break
    else:
        print('Tente Novamente')
        
print(f'{hora}h {minuto}m {segundo}s')