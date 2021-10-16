#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a distancia percorrida:  '))
d = int(input('Por quantos dias o carro ficou alugado? '))
pkm = km * 0.15
pd = d * 60

print('Voce tera que pagar R$ {:.2f} pela quilometragem e R${:.2f} pelos dias que ficou com o carro.'
      ' O valor total da sua conta ficou em R$ {:.2f}'.format(pkm, pd, pkm + pd ) )