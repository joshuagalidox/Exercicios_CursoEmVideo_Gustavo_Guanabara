'''Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem
no final, de acordo com a media atingida:
- Media abaixo de 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO
- Media 7.0 ou superior: APROVADO'''

n1 = float(input('{}Digite a primeira nota: '.format('\n')))
n2 = float(input('{}Digite a segunda nota: '.format('\n')))
media = (n1 + n2)/2

if media >= 7.0:
  print('{}{}A média do aluno foi de {} e por isso ele está APROVADO!{}'.format('\n', '\033[1;32;40m', media, '\033[m'))
elif media < 5.0:
  print('{}{}A média do aluno foi de {} e por isso ele está REPROVADO!{}'.format('\n', '\033[1;31;40m', media, '\033[m'))
else:
  print('{}{}A média do aluno foi de {} e por isso ele está EM RECUPERAÇÃO!{}'.format('\n', '\033[1;33;40m', media, '\033[m'))
print('{}Estudar regularmente é a melhor maneira de se manter preparado!{}'.format('\n', '\n'))
    