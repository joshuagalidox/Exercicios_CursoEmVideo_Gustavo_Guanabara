'''Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas 
podem ou nao formar um triangulo. (pesquisar principio matematico)'''

'''Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre 
maior que a medida do terceiro, então, eles podem formar um triângulo.'''

a = float(input('\n Digite o primeiro valor: '))
b = float(input('\n Digite o segundo valor: '))
c = float(input('\n Digite o terceiro valor: '))
if (a + b) > c and (b + c) > a and (a + c ) >b:
  print('\nCom esses tres segmentos de reta é possível formar um triangulo\n')
else:
  print('\nCom esses tres segmentos de reta não é possível formar um triangulo\n')
  print('\n === FIM === \n')