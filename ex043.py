peso = float(input('QUAL O SEU PESO: '))
altura = float(input('QUAL A SUA ALTURA: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('VOCE ESTA ABAIXO DO PESO')
elif imc < 25:
    print('VOCE ESTA NO PESO IDEAL')
elif imc < 30:
    print('VOCE EM ESTADO DE SOBREPESO')
elif imc < 40:
    print('VOCE ESTA OBESO')
else:
    print('VOCE ESTA EM ESTADO DE OBESIDADE MORBIDA')
print('TENDO {}m DE ALTURA COM {}kg, SEU IMC É DE {:.1f}'.format(altura, peso, imc))