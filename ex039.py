'''Faça um programa que leia o ano de nascimento de um jove e informa, de acordo com sua idade:
- Se ele ainda vai se alistar no serviço militar
- Se é a hora de se alistar
- Se ja passou do tempo de alistamento
Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo'''

from datetime import date

ano = int(input('\nDigite o ano do seu nascimento: '))
hoje = date.today().year
idade = hoje - ano

if idade < 18:
  print('Faltam {} anos para que voce tenha que se alistar. '.format(18-idade))
elif idade > 18:
  print('{}ATENÇÃO: O seu tempo de alistamento expirou há {} anos. Procure o servico militar imediatamente! {}'.format('\033[1;31;40m', idade-18 ,  '\033[0;m'))
else:
  print('Está hora de se alistar! Procure o serviço militar ainda esse ano.')
print('\nServiço militar, um dever cívico do cidadao brasileiro.\n')