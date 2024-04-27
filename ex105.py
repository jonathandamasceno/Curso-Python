def notas(*nota, sit=False):
    '''
    -> Função para analisar notas e situações de alunos.
    :param nota: Recebe as notas (pode ser quantas quiser).
    :param sit: Opcional, indica se irá mostrar ou não a situação.
    :return: Retorna o dicionário com todas as informações.
    '''
    global maior
    global menor
    dados = {'total': nota}
    media = 0
    c = 0
    for v in dados.values():
        for i in v:
            media += i
            c += 1
            if c == 1:
                maior = menor = i
            else:
                if i > maior:
                    maior = i
                if i < menor:
                    menor = i
    media = media / c
    dados['total'] = len(nota)
    dados['Maior'] = maior  # podia usar o max(nota)
    dados['Menor'] = menor  # podia usar o min(nota)
    dados['Media'] = media  # podia usar sum(nota) / len(nota
    if sit:
        if media >= 7:
            dados['Situação'] = 'BOA'
        elif 4 <= media >= 6:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'RUIM'
    return dados


maior = menor = 0
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)