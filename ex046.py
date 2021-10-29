'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até zero, com 
pausa de 1 segundo entre eles.'''

import emoji as e
from time import sleep

print('\n', 25*'#@', ' REVEILLÓN 2021 ', 25*'#@')
print('\nContagem Regressiva')
for c in range(10, -1, -1 ):
  print('{:2}'.format(c), e.emojize(' :clock12:', use_aliases= True))
  sleep(1.0)
print(e.emojize('\n:fireworks::fireworks::fireworks: FELIZ ANO NOVO! :fireworks::fireworks::fireworks: \n', use_aliases=True))