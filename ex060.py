'''### Ex060 - Fatorial
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex.: 5! = 5x4x3x2x1 = 120'''

from math import factorial
num = int(input('Digite um número: '))
cont = num
while not cont == 0:
  print('{}'.format(cont), end= ' ')
  print(' x ' if cont > 1 else ' = ', end= ' ')
  cont = cont - 1
print(factorial(num))
