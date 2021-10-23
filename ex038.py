'''Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Nao existe valor maior, os dois sao iguais'''

n1 = int(input('\nDigite o primeiro número:'))
n2 = int(input('\nDigite o segundo número: '))

if n1 > n2 :
  print('\nO primeiro valor ({}) é maior que o segundo ({}) .'.format(n1, n2))
elif n2 > n1: 
  print('O segundo valor ({}) é maior que o primeiro ({}) .'.format(n2, n1) )
else:
  print('Nao existe valor maior. Os dois sao iguais') 
print('\n---FIM---\n')