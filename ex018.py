import math
valor_angulo = int(input('DIGITE O ANGULO: '))
sen = math.sin(math.radians(valor_angulo))
cos = math.cos(math.radians(valor_angulo))
tan = math.tan(math.radians(valor_angulo))

#tem que converter pra radianos pra funcionar

print('o seno de {} é {:.2f}'.format(valor_angulo, sen))
print('o cosseno de {} é {:.2f}'.format(valor_angulo, cos))
print('a tangente de {} é {:.2f}'.format(valor_angulo, tan))
