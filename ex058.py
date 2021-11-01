'''### Ex058 - Jogo da Advinhaçao V2.0

Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep
nc = randint (0,10)
nu = 99
cont = 1
print('\n\n### JOGO DA ADVINHAÇÃO ### \n\n'
      '>>Seu computador escolherá um numero entre 0 e 10. \n')
sleep(1.00)
while not nu == nc:
  nu = int(input('\nTente adivinhar o número que o computador escolheu, digitando um número: '))
  print ('\nProcessando...')
  sleep(1.00)
  if nu == nc and cont == 1:
    print('{}{}Você me venceu de primeira! PARABÉNS! {}'.format('\n', '\033[1;32;40m', '\033[m'))
  elif nu == nc and cont > 1:
    print('{}{}Até que enfim voce acertou! Foram preciso {} tentativas para me vencer.{}'.format('\n', '\033[1;33;40m', cont, '\033[m'))
  else:
    print('{}{}Voce errou! Tente novamente!{}{}'.format('\n', '\033[1;31;40m', '\033[m', '\n'))
    cont += 1
print('\nFIM')
