nome = str(input('DIGITE SEU NOME: ')).strip()
primeiro_nome = nome.split()[0]

# da pra fazer assim tb
# len(nome) - nome.count(' ')
# nome.find(' ')


print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome, len(primeiro_nome)))
nome = nome.replace(' ', '')
print('Seu nome tem {} letras'.format(len(nome)))

