'''Faça um programa que leia o peso de 5 pessoas e no final, mostre qual  foi o maior e o menor peso lidos'''

pessoas = []
for n in range (1,6):
  pesos = float(input('{}Digite o pessoa da pessoa numero {}: '.format('\n', n)))
  pessoas.append(pesos)
x = sorted(pessoas)
print('{}O maior peso registrado foi {}kg enquanto que o menor foi de {}kg. {}'.format('\n', x[4], x[0], '\n'))