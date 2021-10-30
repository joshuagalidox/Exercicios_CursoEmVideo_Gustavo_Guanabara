'''Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500'''

s = 0
x = 0
l = []
for c in range(1, 501, 1):
  if c % 3 == 0:
    s = s + c # ou s+=c
    x = x+1
    l.append(c)
  else:
    s == s

print('{}A soma dos {} múltiplos de 3 entre 1 e 500 equivale a {}{}'.format('\n', x, s, '\n'))
print(l, end = ' ')

print('Fim')
    