'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
'''Pesquisa: Ano bissexto é um ano que é exatamente divisível por quatro, 
exceto para anos que são exatamente divisíveis por 100, 
mas esses anos centuriais são anos bissextos se forem exatamente divisíveis por 400'''

print('\n {:^24s}'.format('### ANO BISSEXTO? ###\n'))
ano = int(input('Digite qual ano deseja checar: '))

if (ano%4)==0 and (ano%100) == 0 and (ano%400) == 0:
  print('{} é um ano bissexto'.format(ano) )
elif (ano%4)==0 and (ano%100)>0:
  print('{} é um ano bissexto'. format(ano))
else:
  print('{} não é um ano bissexto'.format(ano))
print('\n{:^24s}\n'.format('### FIM ###'))