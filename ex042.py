'''Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
- Equilatero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

'''Ex035: Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas 
podem ou nao formar um triangulo. (pesquisar principio matematico)'''

'''Condiçoes: Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre 
maior que a medida do terceiro, então, eles podem formar um triângulo.'''

m1 = float(input('{}Digite a primeira medida: '.format('\n')))
m2 = float(input('{}Digite a segunda medida: '.format('\n')))
m3 = float(input('{}Digite a terceira medida: '.format('\n')))

if (m1 + m2) > m3 and (m1+m3) > m2 and (m2 + m3) > m1:
  print('{}Com as medidas que você propôs, É POSSÍVEL formar um triângulo'.format('\n'))
  if m1 == m2 ==m3:
    print('{}O triangulo formado por essas tres medidas seria um TRIANGULO EQUILATERO.{}'.format('\n', '\n'))
  elif m1 != m2 != m3:
    print('{}O triangulo formado por essas tres medidas seria um TRIANGULO ESCALENO.{}'.format('\n', '\n'))
  else:
    print('{}O triangulo formado por essas tres medidas seria um TRIANGULO ISÓSCELES.{}'.format('\n', '\n'))
else:
  print('{}Com as medidas que você propôs, NÃO É POSSÍVEL formar um triângulo. {}'.format('\n', '\n'))  