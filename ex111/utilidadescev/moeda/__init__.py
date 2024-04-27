def dobro(n, form=False):
    db = n * 2
    if form:
        return moeda(db)
    else:
        return db


def metade(n, form=False):
    mt = n / 2
    if form:
        return moeda(mt)
    else:
        return mt


def aumentar(n, pct, form=False):
    pct = pct / 100
    aumento = n + (n * pct)
    if form:
        return moeda(aumento)
    else:
        return aumento


def diminuir(n, pct, form=False):
    pct = pct / 100
    decre = n - (n * pct)
    if form:
        return moeda(decre)
    else:
        return decre


def moeda(n):
    n = f'R${n:.2f}'.replace('.', ',')
    return n


def resumo(p, aum=10, dec=5):
    titulo('RESUMO DO VALOR')
    print(f'Preço Analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{dec}% de aumento: \t{diminuir(p, dec, True)}')
    print('-' * 30)
    # \t faz ficar pique tabuada


def titulo(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)
