salario = float(input('DIGITE SEU SALARIO: '))
if salario > 1250:
    novo_sal = salario + (salario * 0.1)
    porc = 10
else:
    novo_sal = salario + (salario * 0.15)
    porc = 15
print('seu novo salario com um aumento de {}% será de R${:.2f}'.format(porc, novo_sal))