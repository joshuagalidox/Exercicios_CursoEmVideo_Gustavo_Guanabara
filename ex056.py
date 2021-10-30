'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A media de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres tem menos de 20 anos'''

Funder20 = 0
IMvelho = 0
NMvelho = 0
idade = 0
for c in range (1,5):
  n = input('{}Digite o nome da pessoa numero {}: '.format('\n', c)).strip()
  i = int(input('{}Digite a idade de {}: '.format('\n', n)))
  s = input('{}Digite o sexo de {}: [M / F] '.format('\n', n)).strip().upper()
  idade = idade + i
  if i > IMvelho and s == 'M':
    IMvelho = i
    NMvelho = n
  if i <20 and s == 'F'  :
    Funder20 = Funder20 +1
   
print('{}A média de idade do grupo é de {} anos.{} '.format('\n', idade/ c, '\n'))
print('O homem mais velho chama-se {} e ele tem {} anos de idade.{}'.format(NMvelho, IMvelho, '\n'))
print('Esse grupo tem {} mulheres com menos de 20 anos.{}'.format(Funder20, '\n'))