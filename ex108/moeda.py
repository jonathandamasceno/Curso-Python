def dobro(n):
    db = n * 2
    return db


def metade(n):
    mt = n / 2
    return mt


def aumentar(n, pct):
    pct = pct / 100
    aumento = n + (n * pct)
    return aumento


def diminuir(n, pct):
    pct = pct / 100
    decre = n - (n * pct)
    return decre


def moeda(n):
    n = f'R${n:.2f}'.replace('.', ',')
    return n

