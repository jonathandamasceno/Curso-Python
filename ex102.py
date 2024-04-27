def fatorial(n, show=False):
    f = 1
    c = n
    while c >= 1:
        if show: # não preciso colocar a variavel booleana pq já tem lá em cima
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
        c -= 1
    return f


print(fatorial(5, show=True))
print(fatorial(5, show=False))
