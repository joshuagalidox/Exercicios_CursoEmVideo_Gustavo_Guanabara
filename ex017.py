#Faca um programa que ;leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math

'''ca = int(input('Digite a medida do Cateto Adjacente : '))
co = int(input('Digite a medida do Cateto Oposto: '))

caq = math.pow(ca, 2)
coq = math.pow(co, 2)

h = math.sqrt(caq + coq)

print('A medida da hipotenusa é : {}'. format(h))'''


from math import hypot

ca = float(input('Digite a medida do cateto adjacente: '))
co = float(input('Digite a medida do cateto oposto: '))
h = hypot(ca, co)

print('A medida da hipotenusa é : {}'. format(h))