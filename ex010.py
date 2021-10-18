'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
 e mostre quantos dolares ela pode comprar (Considere USD 1,00 = R$ 3,27)'''

d = float(input('Digite quanto em R$ voce tem na carteira: R$'))
print('Com esse dinheiro voce pode comprar {:.2f} dólares americanos'. format(d/3.27))