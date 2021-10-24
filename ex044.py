'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e 
condicao de pagamento:
- a vista dinheiro / cheque: 10% de desconto
- a vista no cartao: 5% de desconto
- em até 2x no cartao: preço normal
- 3x ou mais no cartão: 20% de juros'''

from time import sleep

p = float(input('{}Digite o preço do produto: '.format('\n')))
sleep (1.0)
print('{} 1 - a vista dinheiro / cheque {} 2 - a vista no cartao {} 3 - em até 2x no cartao {} 4 - 3x ou mais no cartão{}'.format('\n', '\n', '\n', '\n', '\n'))
sleep(0.5)
o = int(input('Escolha a forma de pagamento: '))
sleep(0.5)
if o == 1:
  print('{} Para essa forma de pagamento voce terá 10% DE DESCONTO. O valor do produto ficará em R$ {:.2f}'.format('\n', p*(0.90)))
elif o == 2:
  print('{} Para essa forma de pagamento voce terá 5% DE DESCONTO. O valor do produto ficará em R$ {:.2f}'.format('\n', p*(0.95)))
elif o == 3:
  print('{} Para essa forma de pagamento você NÃO TERÁ DESCONTO. O valor do produto ficará em R$ {:.2f}'.format('\n', p))
elif o == 4:
  print('{} Para essa forma de pagamento haverá acréscimo de 20% de juros do seu cartão. O valor do produto ficará em R$ {:.2f}'.format('\n', (p*1.2)))
else:
  print('{}Opção Inválida'.format('\n'))
print('{}Obrigado pela sua preferência!{}'.format('\n', '\n') )   
             
      