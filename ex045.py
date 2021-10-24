'''Crie um programa que faça o comptador jogar Jokenpo com voce'''
'''Regras: Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).'''

from time import sleep
from random import choice
opcoes = [1, 2, 3]
pc = choice(opcoes)
print('{}{}  JOKENPO  {}{}'.format('\n' , '$%&'*5, '$%&'*5, '\n' ))
print('{}🤖: - Vamos jogar uma partida?'.format('\n'))
sleep(0.80)
user = int(input(('{}Escolha a sua opção: {}{}1 - Pedra 🤜{}2 - Papel🤚{}3 - Tesoura🖖{}'.format('\n', '\n', '\n', '\n', '\n', '\n'))))
sleep(0.80)

if  user ==  pc:
  if user == 1:
    print('🤖: - Voce e eu escolhemos Pedra 🤜. Vamos jogar novamente!')
  elif user == 2:
    print('🤖: - Voce e eu escolhemos Papel🤚. Vamos jogar novamente!')
  elif user == 3:
    print('🤖: - Voce e eu escolhemos Tesoura🖖. Vamos jogar novamente!')
else:
  if user ==1 and pc == 2:
    print('🤖: - Voce escolheu Pedra 🤜 e eu escolhi Papel🤚. Papel embrulha a Pedra! VOCE PERDEU!!')
  elif user ==2 and pc == 1:
    print('🤖: - Voce escolheu Papel🤚 e eu escolhi Pedra 🤜. Papel embrulha a Pedra! VOCE VENCEU!!')
  elif user == 2 and pc == 3:
    print('🤖: - Voce escolheu Papel🤚 e eu escolhi Tesoura🖖. Tesoura corta o Papel! VOCE PERDEU!!')
  elif user == 3 and pc == 2:
    print('🤖: - Voce escolheu Tesoura🖖 e eu escolhi Papel🤚. Tesoura corta o Papel! VOCE VENCEU!!')
  elif user == 1 and pc == 3:
    print('🤖: - Voce escolheu Pedra 🤜 e eu escolhi Tesoura🖖. Pedra quebra Tesoura! VOCE VENCEU!!')
  else:
    print('🤖: - Voce escolheu Tesoura🖖 e eu escolhi Pedra 🤜. Pedra quebra Tesoura! VOCE PERDEU!!')
print('{}🤖: - Te vejo na próxima! {}'.format('\n', '\n'))
