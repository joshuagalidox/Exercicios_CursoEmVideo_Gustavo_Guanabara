'''Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500'''

s = 0
for c in range(1, 501, 1):
  if c % 3 == 0:
    s = s + c # ou s+=c
  else:
    s == s
print('A soma dos numeros ímpares entre 1 e 500 equivale a {}'.format(s))
print('Fim')
    