'''### Ex061 - PA 2.0

Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressao usando a esrutura while'''

'''Desenvolva um programa que leio o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao'''

t = int(input('{}Digite o primeiro termo da PA: '.format('\n')))
r = int(input('Digite a razão da PA: '))
c = 0
s = t
pa = []
pa.append(t)
while not c == 10:
  s = s + r
  pa.append(s)
  c = c+1
pastr = str(pa)
print('{}Os 10 primeiros termos da PA são: {}{}'.format('\n', pa, '\n'))