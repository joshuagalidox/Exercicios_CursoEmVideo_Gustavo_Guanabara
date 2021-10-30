'''Desenvolva um programa que leio o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao'''

t = int(input('{}Digite o primeiro termo da PA: '.format('\n')))
r = int(input('Digite a razão da PA: '))
s = t
pa = []
pa.append(t)
for c in range (1, 10):
  s = s + r
  pa.append(s)
pastr = str(pa)
print('{}Os 10 primeiros termos da PA são: {}{}'.format('\n', pa, '\n'))