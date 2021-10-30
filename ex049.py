'''Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for'''

import emoji as e

print('\n############## TABUADA 2.0 ##############\n')
n = int(input('Digite um numero: '))
o = int(input('{}Escolha a operação: {} [1] Adição {} [2] Subtração {} [3] Multiplicação {} [4] Divisão {} Sua escolha: {}'.format('\n','\n', '\n', '\n', '\n', '\n', '\n\n')))
opcoes = ['adição', 'subtração', 'multiplicação', 'divisão']
if o == 1:
  print('{}{}Você escolheu Tabuada de {} do número {}{}.{}'.format( '\n' ,'\033[1;32;40m', opcoes[0], n, '\033[m','\n' ))
  
  for m in range(1, 11, 1):
      if o == 1:
        print(' {:2} + {:2} = {:2}'.format(n, m, n+m))
      elif o == 2:
        print(' {:2} - {:2} = {:2}'.format(n+m, n, (n+m)-n))
      elif o == 3:
        print(' {} x {:2} = {:2}'.format(n, m, n*m))
      elif o ==4:
        print(' {:2} / {:2} = {:2}'.format(n*m, m, (n*m)//n))
elif o == 2:
  print('{}{}Você escolheu Tabuada de {} do número {}{}.{}'.format( '\n' ,'\033[1;32;40m', opcoes[1], n, '\033[m','\n' ))
  for m in range(1, 11, 1):
      if o == 1:
        print(' {:2} + {:2} = {:2}'.format(n, m, n+m))
      elif o == 2:
        print(' {:2} - {:2} = {:2}'.format(n+m, n, (n+m)-n))
      elif o == 3:
        print(' {} x {:2} = {:2}'.format(n, m, n*m))
      elif o ==4:
        print(' {:2} / {:2} = {:2}'.format(n*m, m, (n*m)//n))
elif o == 3: 
  print('{}{}Você escolheu Tabuada de {} do número {}{}.{}'.format( '\n' ,'\033[1;32;40m', opcoes[2], n, '\033[m','\n' ))
  for m in range(1, 11, 1):
      if o == 1:
        print(' {:2} + {:2} = {:2}'.format(n, m, n+m))
      elif o == 2:
        print(' {:2} - {:2} = {:2}'.format(n+m, n, (n+m)-n))
      elif o == 3:
        print(' {} x {:2} = {:2}'.format(n, m, n*m))
      elif o ==4:
        print(' {:2} / {:2} = {:2}'.format(n*m, m, (n*m)//n))
elif o == 4:
  print('{}{}Você escolheu Tabuada de {} do número {}{}.{}'.format( '\n' ,'\033[1;32;40m', opcoes[3], n, '\033[m','\n' ))
  for m in range(1, 11, 1):
      if o == 1:
        print(' {:2} + {:2} = {:2}'.format(n, m, n+m))
      elif o == 2:
        print(' {:2} - {:2} = {:2}'.format(n+m, n, (n+m)-n))
      elif o == 3:
        print(' {} x {:2} = {:2}'.format(n, m, n*m))
      elif o ==4:
        print(' {:2} / {:2} = {:2}'.format(n*m, m, (n*m)//n))

else:
  print('Opçao Invalida')
  
print('\nFIM\n')