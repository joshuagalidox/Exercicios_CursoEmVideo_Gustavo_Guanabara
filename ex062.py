'''### Ex062 - PA 2.1

Melhore o desafio 61, perguntando se ele quer mostrar mais alguns termos. O programa encessa quando ele disser que quer mostrar 0 termos'''

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