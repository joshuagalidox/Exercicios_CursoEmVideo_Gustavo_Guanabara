'''Crie um programa que leia o ano de nascimento de 7 pessoas. 
No final, mostre quantas ainda nao atingiram a maioridade e quantas já sao maiores (maioridade +21)'''

maiores= []
menores = []
for pessoas in range (1,8):
  idade = int(input('{}Digite a idade da pessoa numero {} :'.format('\n', pessoas)))
  if idade >= 21:
    maiores.append(idade)
  else:
    menores.append(idade)
print('{}Considerando o público registrado, {} são maiores de idade (21+) e {} ainda não alcançaram a maioridade.{}'. format('\n', len(maiores), len(menores), '\n'))