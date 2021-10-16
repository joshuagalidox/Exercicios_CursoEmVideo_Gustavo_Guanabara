#Faca um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto

p = float(input('Qual o preço do produto? '))
d = 0.05
print('O novo preço já considerando {}% de desconto é {:.2f}'.format(d*100, p*(1-d)))