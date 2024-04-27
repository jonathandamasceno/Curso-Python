frase = str(input('DIGITE UM FRASE E ANALISAREI SE É UM PALINDROMO: ')).strip().upper()
junto = frase.replace(' ', '')
inverso = ''
for c in range(len(junto) - 1, -1, -1): # nao posso colocar 'junto[0] ou [-1]' tem que ser len(junto)
    inverso += junto[c]
if junto == inverso:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')
print(inverso)