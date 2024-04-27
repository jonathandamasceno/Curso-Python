from math import hypot
cateto_o = float(input('comprimento do cateto oposto: '))
cateto_a = float(input('comprimento do cateto adjacente: '))
print('a hipotenusa é {:.2f}'.format(hypot(cateto_a, cateto_o)))