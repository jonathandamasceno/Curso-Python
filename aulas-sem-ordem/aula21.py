# 1 - > Interactive Help;
# 2 - > docstrings;
# 3 - > Argumentos opcionais;
# 4 - > Escopo de variaveis;
# 5 - > Retorno de resultados.

# dar help() no console pra aprender sobre algumas bibliotecas ou funções
# help(print) <- Tambem serve
# print(input.__doc__) -> documentação inteira da função input()

# manual da função = docstring
# criando um docstring >

def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: Inicio
    :param f: Fim
    :param p: Passo
    :return: Sem Retorno
    '''
    c = i
    while c <= f:
        print(c, end=' ')
        c += p


help(contador)
# parametros opcionais
# se eu colocar valendo zero, se ele nao for digitado o valor dele será aquele


def soma(a=0, b=0, c=0):
    s = a + b + c
    print(s)


soma(1, 3, 7)
soma(1, 3)
# para usar uma variavel global numa função sem criar uma variavel local


def teste(b):
    global a


a = 5
print(a)
# retornando valores > return
