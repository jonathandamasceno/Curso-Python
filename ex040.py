n1 = float(input('DIGITE A PRIMEIRA NOTA: '))
n2 = float(input('DIGITE A SEGUNDA NOTA: '))
media = (n1 + n2) / 2
if media < 6:
    print('VOCÊ NÃO PASSOU, SUA MEDIA FOI {}.'.format(media))
else:
    print('VOCÊ PASSOU, SUA MEDIA FOI {}.'.format(media))