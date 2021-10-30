'''Faca um programa que leia um numero inteiro e diga se ele é ou nao um numero primo'''

n = int(input('\nDigite um numero inteiro: '))
div = []
for c in range (1, n+1):
  if n % c == 0:
    div.append(c)

if n == 1 or len(div) == 2:
  print('{}O numero {} só é divisível por 1 e ele mesmo. Por isso é considerado um número primo.'.format('\n', n))
else:
  print('{}O número {} tem {} divisores e por isso não é considerado um número primo.'.format('\n', n, len(div)))
print('\nFIM\n')