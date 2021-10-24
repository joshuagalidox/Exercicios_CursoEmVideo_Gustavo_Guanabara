'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo: 
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- Entre 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

'''IMC = Peso (kg) / Altura (m) **2'''

print('{}{}{} CALCULADORA DE IMC {}{}{}'.format('\n' , '\033[1;34;40m', '=*-*' * 5 , '=*-*' * 5 , '\033[m' ,'\n' ))

p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))
IMC = p / (a**2)
faixas = ['- Abaixo de 18.5: Abaixo do peso', '- Entre 18.5 e 25: Peso ideal',
          '- Entre 25 até 30: Sobrepeso', '- 30 até 40: Obesidade', '- Acima de 40: Obesidade mórbida']

if  IMC <18.5:
  print('{}Seu IMC é de : {:.2f} e você está na faixa : {}{}{}{}'.format('\n', IMC, '\n','\033[1;31;40m', faixas[0], '\033[m' ))
elif IMC < 25:
  print('{}Seu IMC é de : {:.2f} e você está na faixa : {}{}{}{}'.format('\n', IMC, '\n','\033[1;33;40m', faixas[1], '\033[m' ))
elif IMC <30:
  print('{}Seu IMC é de : {:.2f} e você está na faixa : {}{}{}{}'.format('\n', IMC, '\n','\033[1;33;40m', faixas[2], '\033[m' ))
elif IMC <40:
  print('{}Seu IMC é de : {:.2f} e você está na faixa : {}{}{}{}'.format('\n', IMC, '\n','\033[1;31;40m', faixas[3], '\033[m' ))
else:
  print('{}Seu IMC é de : {:.2f} e você está na faixa : {}{}{}{}'.format('\n', IMC, '\n','\033[1;31;40m', faixas[4], '\033[m' ))

print('{}Mantenha sempre uma rotina de exercícios e alimentação saudável! {}'.format('\n', '\n'))