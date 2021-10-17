'''Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e 
  peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
  O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
  
import random as r
from time import sleep
nc =  r.randint(0, 5)
print('\n\n### JOGO DA ADVINHAÇÃO ### \n\n'
      '>>Seu computador escolherá um numero entre 0 e 5. \n' 
      '>>Tente adivinhar qual o número escolhido pelo seu computador.\n')
sleep(1.20)
print('Computador Pensando....\n')
sleep(1.80)
print('O computador já escolheu seu numero!\n')
nu = int(input('Digite qual numero voce acha que ele escolheu: '))
print('\nCalculando o resultado...\n')
sleep(1.00)
if nc == nu:
  print('PARABÉNS! Seu computador escolheu o número {} e voce advinhou! \n'. format(nc))
else:
  print('VOCE ERROU!Seu computador escolheu o número {}. \n'. format(nc))
  print('\n --- FIM ---\n')