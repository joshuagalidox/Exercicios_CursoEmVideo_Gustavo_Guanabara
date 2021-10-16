
'''023. Faça um programa que leia um numero entre 0 e 9.999 e mostre na tela cada um dos digitos separados.
    Exempplo: Digite um numero: 1834
                Unidade: 4
                Dezena: 3
                Centena: 8
                Milhar: 1 '''

num = int((input('Digite um numero: ')))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print('Analisando o numero {} ...'.format(num))
print('Unidades: {} '.format(u))
print('Dezenas: {} '.format(d))
print('Centenas: {} '. format(c))
print('Milhares: {} '.format(m))

