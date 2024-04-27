# funções em pythão
# def = definir uma funcão
def mostralinha():
    print('-'*30)
# função sem parametro  
    
mostralinha() # executa a função
print(f'{"ola mundo":^30}')
mostralinha()

# função com parametro  
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
mensagem(f'{"PRIMEIRA MENSAGEM":^30}')
mensagem(f'{"SEGUNDA MENSAGEM":^30}')

#função de calculos
def soma (x, y):
    s = x + y
    print(s)
    m = x * y
    print(m)
    sub = x - y
    print(sub)
    div = x / y
    print(div)
    
        
soma(y=81,x=9)   # da pra alterar qual parametro ele pertence

#"empacotamento"
def contador(*num): # ele cria uma tupla 
    print(f'foram mostrados {len(num)} numeros') # len(tupla) - > num
contador(5, 2, 3, 9, 8, 16)