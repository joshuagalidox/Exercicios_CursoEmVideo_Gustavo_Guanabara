'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
Exemplos: Apos a sopa
A sacada da casa
A torre da derrota
anotaram a data da maratona'''

f = str(input('\nDigite uma frase: ').strip().upper())
fse = f.replace(' ', '') #frase sem espaços
print(fse, end = ' ')
print(fse [::-1])
if fse== fse [::-1]:
  print('Palindromo')
else:
  print('Nao Palindromo')
