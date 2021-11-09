'''### Ex059 - Menu de Opçoes

Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa

Seu progrma deverá realizar a operação solicitada em cada caso.'''
from time import sleep
menu = 1
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while not menu == 5:
  menu = int(input('{}Escolha uma opção: {}[1] Somar {}[2] Multiplicar {}[3] Identificar o maior {}[4] Digitar novos valores {}[5] Sair do programa {}{}SUA OPÇÃO >>> '. format('\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n')))
  if menu == 1:
    print('{}A soma de {} e {} é igual a: {}.'.format('\n', n1, n2, n1+n2))
  elif menu == 2:
    print('{}O produto de {} e {} é igual a: {}.'.format('\n', n1, n2, n1*n2))
  elif menu == 3:
    if n1 > n2:
      print('{}{} é maior que {}'.format('\n', n1, n2))
    elif n2 > n1:
      print('{}{} é maior que {}'.format('\n', n2, n1 ))
    else:
      print('{}Os valores digitados são iguais.'.format('\n'))
  elif menu == 4:
    print('{}Reiniciando...{}'.format('\n', '\n'))
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    sleep(0.50)
  elif menu == 5:
     print('{}<<< Fim da aplicação >>>{}'. format('\n', '\n'))
  else:
      print('Opção Inválida. Tente novamente!')
print('{}Calculadora do Josuka. Todos os direitos reservados. 2021{}'.format('\n', '\n'))