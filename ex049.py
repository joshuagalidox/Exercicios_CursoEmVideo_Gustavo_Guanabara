'''Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for'''

import emoji as e

print('\n############## TABUADA 2.0 ##############\n')
n = int(input('{}Digite um numero: '.format('\n')))
o = int(input('{}Escolha a operação: {} [1] Adição {} [2] Subtração {} [3] Multiplicação {} [4] Divisão {} Sua escolha: '.format('\n','\n', '\n', '\n', '\n', '\n\n')))
for m in range(1, 11, 1):
  if o == 1:
    print(' {:2} + {:2} = {:2}'.format(n, m, n+m))
  elif o == 2:
    print(' {:2} - {:2} = {:2}'.format(n+m, n, (n+m)-n))
  elif o == 3:
    print(' {} x {:2} = {:2}'.format(n, m, n*m))
  elif o ==4:
    print(' {:2} / {:2} = {:2}'.format(n*m, m, (n*m)//n))
    
print('FIM')