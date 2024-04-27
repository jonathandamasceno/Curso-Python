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

