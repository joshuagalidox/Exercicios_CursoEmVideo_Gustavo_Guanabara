'''Faca um programa que leia um angulo e mostre na tela o valor do seno, cosseno e tangente
desse angulo'''

import math as m

a = int(input('Digite o valor de um angulo: '))
s = m.sin(m.radians(a))
cos = m.cos(m.radians(a))
t = m.tan(m.radians(a))

print('Num angulo de {} graus, o valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'. format(a, s, cos, t))