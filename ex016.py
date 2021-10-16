'''Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua
porcao inteira. #Exemplo:   Digite um numero
                            O numero 6.127 tem a parte inteira 6'''

import math
n = float(input('Digite um numero: '))
a = math.trunc(n)

print('O numero {} tem a parte inteira {}'. format(n, a))

