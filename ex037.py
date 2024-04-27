numero = int(input('DIGITE UM NUMERO PRA CONVERSÃO: '))
opcao = int(input('''ESCOLHA A CONVERSÃO:
[1] BINARIO                
[2] HEXADECIMAL
[3] OCTADECIMAL
QUAL A SUA ESCOLHA: '''))
if opcao == 1:
    print('O numero {} em binario é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O numero {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
elif opcao == 3:
    print('O numero {} em octadecimal é {}'.format(numero, oct(numero)[2:]))
else:
    print('Escolha de 1 a 3. Programa finalizado.')
