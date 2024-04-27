sexo = str(input('INFORME SEU SEXO [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('OPÇÃO INVALIDA. INFORME SEU SEXO [M/F]: ')).strip().upper()
print('Sexo {} registrado. Bom dia.'.format(sexo))