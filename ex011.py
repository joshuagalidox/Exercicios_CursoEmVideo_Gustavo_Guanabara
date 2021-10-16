#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
# e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta
#pinta uma area de 2m2.

l = float(input('Digite a largura da sua parede: '))
h = float(input('Digite a altura da sua parede: '))
a = l*h
t = 2 #Cada litro de tinta pinta 2 m2

print('A sua parede tem uma área de {} m2 '.format(a))
print('Para pintar essa parede, voce precisará de {:.2f} litros de tinta'.format(a/t))