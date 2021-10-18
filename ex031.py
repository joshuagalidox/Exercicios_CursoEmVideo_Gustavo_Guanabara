'''Desenvolva um programa que pergunte a distanca de uma viagem em KM. 
Calcule o preco da passagem, cobrando R$0,50 por KM para viagens de até 200km e 
R$0,45 para viagens mais longas.'''

d = float(input('Qual a distancia em KM da viagem que deseja fazer? '))
t1 = d*0.50
t2 = d*0.45
if d<=200.00:
  print('\nTARIFA 01: O valor da passagem será de R${:.2f} .'.format(t1))
else:
  print('\nTARIFA 02: O valor da passagem será de R${:.2f}'.format(t2))
print('\n---FIM---\n')