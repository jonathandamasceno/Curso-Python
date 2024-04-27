import menu as menuconfig
def lerNome():
    while True:
        n = input('Digite seu nome completo: ')
        if n.isnumeric():
            print('Nome Inválido. Digite novamente.')
        else:
            return n.title() 
        
   
def lerIdade():
    while True:
        try:
            i = int(input('Digite sua idade: '))
        except ValueError:
            print('Idade Inválida. Digite novamente.')
        else:
            return i 
    
    
def Cadastro():
    print('-' * 40)
    print(f'{"-> Cadastrar Nova Pessoa.":^40}')
    print('-' * 40)
    nome = lerNome()
    idade = lerIdade()  
    with open("dados.txt", "a", encoding="utf-8") as dados:
        dados.write(f"{nome:<30}{idade:>3} anos \n")

    return menuconfig.escolha()
