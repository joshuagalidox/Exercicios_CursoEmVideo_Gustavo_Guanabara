'Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor'
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

l = [n1, n2, n3]
l.sort()
print('\nO maior dos numeros digitados é o {} .\n'.format(l[2]))
print('O menor dos numeros digitados é o {} .\n'.format(l[0]))