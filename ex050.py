'''Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for impar, desconsidere-o.'''

l = [ ]
s = 0

for c in range(1, 7):
  n = int(input('\nDigite um numero: '))
  if n % 2 == 0:
    l.append(n)
    s = n + s
  else:
    s = s 
lstr = str(l)
print('\nOs numeros pares digitados foram: {} e sua soma é equivalente a {}\n'.format(lstr[1:8], s))