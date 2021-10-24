'''A Confederaçao NAcional de Nataçao precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria de acordo com a idade:
- Ate 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Senior
- Acima: Master'''

from datetime import date
nasc = int(input('{}Digite a data de nascimento do atleta: '.format('\n')))
hoje = date.today().year
idade = hoje - nasc
categoria = ['=> Ate 9 anos: Mirim', '=> Até 14 anos: Infantil', '=> Até 19 anos: Junior', '=> Até 20 anos: Senior','=> 20+: Master' ]
if idade <= 9:
  print('{}O atleta tem {} anos e  pertence a categoria: {}{}{}{}'.format('\n', idade, '\n' ,'\033[1;33;40m' , categoria[0], '\033[m')) 
elif idade <= 14:
   print('{}O atleta tem {} anos e pertence a categoria: {}{}{}{}'.format('\n', idade, '\n' ,'\033[1;33;40m' , categoria[1], '\033[m')) 
elif idade <= 19:
   print('{}O atleta tem {} anos e pertence a categoria: {}{}{}{}'.format('\n', idade, '\n' ,'\033[1;33;40m' , categoria[2], '\033[m')) 
elif idade <= 20:
   print('{}O atleta tem {} anos e pertence a categoria: {}{}{}{}'.format('\n', idade, '\n' ,'\033[1;33;40m' , categoria[3], '\033[m'))
else:
   print('{}O atleta tem {} anos e pertence a categoria: {}{}{}{}'.format('\n', idade, '\n' ,'\033[1;33;40m' , categoria[4], '\033[m'))  
print('{}Confederaçao Nacional de Natação{}'.format('\n', '\n'))

