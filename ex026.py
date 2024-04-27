frase = str(input('DIGITE UMA FRASE: ')).strip().upper()
print('A LETRA A APARECE {} VEZES'.format(frase.count('A')))
print('A PRIMEIRA LETRA A APARECEU NA POSIÇÃO {}'.format(frase.find('A') + 1))
print('A ULTIMA LETRA A APARECEU NA POSIÇÃO {}'.format(frase.rfind('A') + 1))