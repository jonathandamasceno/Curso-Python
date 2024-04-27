num1 = int(input('DIGITE UM NUMERO: '))
num2 = int(input('DIGITE OUTRO NUMERO: '))
escolha = 0
maior = 0
while escolha != 5:
    escolha = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
SUA ESCOLHA: '''))
    
    if escolha == 1: 
        soma = num1 + num2
        print('{} + {} = {}'.format(num1 , num2, soma))
    elif escolha == 2: 
        mult = num1 * num2
        print('{} X {} = {}'.format(num1 , num2, mult))
    elif escolha == 3: 
        if num1 > num2:
            print('{} é maior.'.format(num1))
        if num2 > num1:
            print('{} é maior.'.format(num2))
        else:
            print('São numeros iguais')
    elif escolha == 4: 
        num1 = int(input('DIGITE UM NUMERO: '))
        num2 = int(input('DIGITE OUTRO NUMERO: '))
        
        
print('Fim do programa.')