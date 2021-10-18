'''Escreva um programa que pergunte o salario de um funcionário e calcule o valor de seu aumento. 
Para salarios superiores a R$1.250, calcule um aumento de 10%. 
Para inferiores ou iguais, o aumento é de 15%'''

print('{:^24s}'.format('\n### Qual aumento? ### \n'))
s = float(input('Qual o salario do funcionário? '))
print('O salario terá um reajuste de 10% ,e passará a ser de R${:.2f}'.format(s*1.10) if s>1250 else 'O salário tera um reajuste de 15%, e passará a ser de R${:.2f} .'.format(s*1.15))
print('\n === FIM ===\n')