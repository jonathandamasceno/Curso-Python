def voto(data):
    from datetime import date
    idade = date.today().year - data
    if idade >= 18 and idade <= 60:
        print(f'Com {idade} anos: ', end='')
        print('VOTO OBRIGATÓRIO')
    elif idade < 16:
        print(f'Com {idade} anos: ', end='')
        print('NÃO VOTA')
    elif 16 <= idade < 18 or idade > 60:
        print(f'Com {idade} anos: ', end='')
        print('VOTO OPCIONAL')


print('-'*30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
print('-'*30)
