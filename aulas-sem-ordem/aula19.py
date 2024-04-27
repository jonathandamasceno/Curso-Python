# Dicionários {}
'''
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome']) == Pedro
print(dados['idade']) == 25

criando outro termo
dados['sexo'] = 'M' (é como se fosse um .append())

apagando
del dados['nome']

print(dados.values()) tudo que tá dentro ('Pedro', 25)
print(dados.keys()) o identificador (nome, idade, sexo)
print(dados.items()) ambos

for chave (key), valor (value) in dados.items():
    print(f'O {chave) é {valor}')
                nome     Pedro
                idade      25
                sexo       M
                
da pra colocar dicionario em lista
lista [[dados]]


se quiser dar um print simples, tem que usar aspas duplas
ex.: print(f'O {dados["nome"]} tem {dados["idade"]} anos.')




ao nves de copiar assim -> [:], nos dicionarios tem o .copy()
'''