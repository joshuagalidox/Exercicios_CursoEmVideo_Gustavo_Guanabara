'''Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual 
sera a base de conversao:
1. para binário
2. para octal
3. para hexadecimal'''
print('\n')
print('#='*5, 'CONVERSOR DE BASES', '#='*5)
print('\n')
num=int(input(' Digite um número: '))
opc = int(input(' \nEscolha para qual base deseja converter: \n 1 - binario \n 2 - octal \n 3 - hexadecimal\n'))
b = str(bin(num))
o = str(oct(num))
x = str(hex(num))
if opc == 1:
  print('\nO número {} convertido para a base binaria é representado como {}'.format(num, b [2: ]))
elif opc == 2:
  print('\nO número {} convertido para a base octal é representado como {}'.format(num, o [2: ]))
elif opc == 3:
  print('\nO número {} convertido para a base hexadecimal é representado como {}'.format(num, x [2: ]))
else:
  print('\nOpçao inválida\n')
print('\nFIM\n')