'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
O programa vai perguntar o valor da casa, o salario do comprador e em quantos  anos ele vai pagar. 
Calcule o valor da prestaçao mensal, sabendo que ela nao pode exceder 30%  do salario ou entao 
o emprestimo sera negado'''

print('\n')
print('=*='*16)
print( '#@'*5, 'SIMULADOR DE FINANCIAMENTO', '#@'*5,)
print('=*='*16)
print('\n')
salario = float(input('\033[1;34;40m 01 - Informe o valor do seu salário mensal: '))
preco = float(input('\033[1;33;40m 02 - Digite o valor do imóvel: '))
anos = float(input('\033[1;34;40m 03 - Em quanto anos voce deseja financiar o imóvel? '))
vparcela = preco / (anos*12)

if vparcela <= (salario*0.30):
  print('\n{}PARABENS! Seu financiamento foi aprovado!'.format('\033[1;32m'))
  print('\n{}Seu financiamento será feito em {} parcelas de R${:.2f}{}'.format('\033[1;32;40m', anos*12, vparcela, '\033[m'))
else:
  print('\n{}Seu financiamento foi reprovado, pois o valor da parcela supera 30 % do seu salario. {}'.format('\033[1;31m', '\033[m'))
print('Obrigado por ser nosso cliente!\n')